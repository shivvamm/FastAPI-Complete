from fastapi import FastAPI
import models
from database import engine
from routers import auth,todos,admin, users


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
