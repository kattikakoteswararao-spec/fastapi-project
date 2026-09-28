from fastapi import FastAPI
from app.routers import users
from app.database.database import  Base, engine
from app.models import user

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="User Management API",
    description="My first FastAPI project",
    version="1.0.0"
)

app.include_router(users.router)



@app.get("/")
def home():
    return {
        "message": "FastAPI is working!"
    }
    