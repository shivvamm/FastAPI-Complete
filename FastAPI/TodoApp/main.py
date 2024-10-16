from fastapi import FastAPI
from .models import Base
from .settings import engine
from .routers import auth,todos,admin, users

Base.metadata.create_all(bind=engine)

app = FastAPI()


#Mock test check
@app.get("/healthly/")
async def health_check():
    return {"status": "Healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
