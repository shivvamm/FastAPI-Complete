from fastapi import FastAPI, Request, status
from .models import Base
from .settings import engine
from .routers import auth,todos,admin, users

from fastapi.staticfiles import StaticFiles 
from fastapi.responses import RedirectResponse
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.mount("/static",StaticFiles(directory="TodoApp/static"),name="static")

@app.get("/")
def test(request: Request):
    return RedirectResponse(url="/todos/todo-page",status_code=status.HTTP_302_FOUND)


#Mock test check
@app.get("/healthly/")
async def health_check():
    return {"status": "Healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
