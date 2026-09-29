from sqlalchemy.orm import Session

from app.repositories import user_repository


def create_user(db: Session, name: str, email: str, age: int):
    return user_repository.create_user(
        db=db,
        name=name,
        email=email,
        age=age
    )


def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    name: str | None = None
):
    return user_repository.get_users(
        db=db,
        skip=skip,
        limit=limit,
        name=name
    )


def get_user(db: Session, user_id: int):
    return user_repository.get_user_by_id(db, user_id)


def update_user(
    db: Session,
    user_id: int,
    name: str,
    email: str,
    age: int
):
    return user_repository.update_user(
        db=db,
        user_id=user_id,
        name=name,
        email=email,
        age=age
    )


def delete_user(db: Session, user_id: int):
    return user_repository.delete_user(db, user_id)