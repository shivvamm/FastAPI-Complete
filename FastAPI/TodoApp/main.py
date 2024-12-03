from fastapi import FastAPI, Request
from .models import Base
from .settings import engine
from .routers import auth,todos,admin, users
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 

Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="TodoApp/templates")

app.mount("/static",StaticFiles(directory="TodoApp/static"),name="static")

@app.get("/")
def test(request: Request):
    return templates.TemplateResponse('home.html',{"request":request})


#Mock test check
@app.get("/healthly/")
async def health_check():
    return {"status": "Healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
