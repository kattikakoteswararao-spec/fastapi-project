from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate, UserUpdate
from app.services import user_service


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return user_service.create_user(
        db=db,
        name=user.name,
        email=user.email,
        age=user.age
    )


@router.get("/")
def get_users(
    db: Session = Depends(get_db)
):
    return user_service.get_users(db)


@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = user_service.get_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put("/{user_id}")
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    updated_user = user_service.update_user(
        db=db,
        user_id=user_id,
        name=user.name,
        email=user.email,
        age=user.age
    )

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    deleted_user = user_service.delete_user(db, user_id)

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }