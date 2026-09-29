from sqlalchemy.orm import Session

from app.models.user import User


def create_user(db: Session, name: str, email: str, age: int):
    new_user = User(
        name=name,
        email=email,
        age=age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    name: str | None = None
):
    query = db.query(User)

    if name:
        query = query.filter(User.name.ilike(f"%{name}%"))

    return query.offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, name: str, email: str, age: int):
    user = get_user_by_id(db, user_id)

    if user:
        user.name = name
        user.email = email
        user.age = age

        db.commit()
        db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    if user:
        db.delete(user)
        db.commit()

    return user