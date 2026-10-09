from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from database import SessionLocal
from models.user import User
import secrets

security = HTTPBasic()


def get_current_user(
    credentials: HTTPBasicCredentials = Depends(security)
):
    db = SessionLocal()

    try:
        user = db.query(User).filter(
            User.username == credentials.username
        ).first()

        if user is None or not secrets.compare_digest(
            user.password, credentials.password
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password",
                headers={"WWW-Authenticate": "Basic"}
            )

        return {
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    finally:
        db.close()


def require_role(required_role: str):
    def check_role(
        current_user: dict = Depends(get_current_user)
    ):
        if current_user["role"] != required_role:
            raise HTTPException(
                status_code=403,
                detail="You do not have permission"
            )

        return current_user

    return check_role