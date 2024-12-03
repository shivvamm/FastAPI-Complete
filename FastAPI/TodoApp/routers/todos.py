from fastapi import APIRouter,Depends,HTTPException,Body,Path,Query, Request
from ..settings import SessionLocal
from typing import Annotated
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from ..models import Todos
from starlette import status
from pydantic import BaseModel,Field
from .auth import get_current_user
# from langchain_groq import ChatGroq
import os 
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

load_dotenv()

# llm = ChatGroq(
#     temperature=0.0,
#     groq_api_key=os.getenv("GROQ_API_KEY"),
#     model_name="llama3-70b-8192",
# )


router = APIRouter(
    prefix="/todos",
    tags=['todos']
)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TodoRequest(BaseModel):
    title:str= Field(min_length=3)
    description:str = Field(min_length=3,max_length=100)
    priority:int =  Field(gt=0,lt=6)
    complete:bool
    due_date:str


def redirect_to_login():
    redirect_response = RedirectResponse(url="/auth/login-page",status_code=status.HTTP_302_FOUND)
    redirect_response.delete_cookie(key="access_token")
    return redirect_response

class PromptTodoRequest(BaseModel):
    prompt:str

db_dependency = Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]

tempaltes= Jinja2Templates(directory="TodoApp/templates")


## Pages

@router.get("/todo-page")
async def render_todo_page(request:Request, db:db_dependency):
    try:
        user = await get_current_user(request.cookies.get('access_token'))
        if user is None:
            return redirect_to_login()
        todos = db.query(Todos).filter(Todos.owner_id == user.get('id')).all()
        print(todos)
        return tempaltes.TemplateResponse('todo.html',{"request":request,"todos":todos,"user":user})
    except:
        return redirect_to_login()

## Todos

@router.get("/",status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()




@router.get('/todo/{todo_id}',status_code=status.HTTP_200_OK)
async def read_todo(user:user_dependency,db:db_dependency,
                    todo_id:int=Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail='Todo not found')





@router.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(user:user_dependency,db:db_dependency,
                todo_request:TodoRequest):
    print(user)
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")
    
    todo_model = Todos(**todo_request.model_dump(),owner_id = user.get('id'))

    db.add(todo_model)
    db.commit()



@router.post("/todo/prompt",status_code=status.HTTP_201_CREATED)
async def create_todo_by_prompt(user:user_dependency,db:db_dependency,
                todo_request:PromptTodoRequest):
    print(user)
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")
    
    todo_model = Todos(**todo_request.dict(),owner_id = user.get('id'))

    db.add(todo_model)
    db.commit()



@router.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user:user_dependency,db:db_dependency,
                    todo_request:TodoRequest,todo_id:int=Path(gt=0)):
    
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")
    

    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found')
    todo_model.title = todo_request.title
    todo_model.description= todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    todo_model.due_date = todo_request.due_date

    db.add(todo_model)
    db.commit()




@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user:user_dependency,db:db_dependency,
                      todo_id:int=Path(gt=0)):

    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found')
    db.query(Todos).filter(Todos.id == todo_id).\
        filter(Todos.owner_id == user.get('id')).delete()

    db.commit()