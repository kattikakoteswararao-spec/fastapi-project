from app.core.exception_handlers import general_exception_handler
from app.core.logging_config import setup_logging

setup_logging()
from fastapi import FastAPI
from app.routers import users
from app.database.database import  Base, engine
from app.models import User, Document

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="User Management API",
    description="My first FastAPI project",
    version="1.0.0"
)
app.add_exception_handler(Exception, general_exception_handler)
app.include_router(users.router)



@app.get("/")
def home():
    return {
        "message": "FastAPI is working!"
    }
    