from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models.user import User
from schemas.user_schema import UserCreate, UserLogin

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        db.close()
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = User(
        fullname=user.fullname,
        email=user.email,
        username=user.username,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {
        "message": "Registration successful",
        "username": user.username
    }


@router.post("/login")
def login_user(user: UserLogin):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if existing_user.password != user.password:
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    db.close()

    return {
        "message": "Login successful",
        "username": existing_user.username
    }