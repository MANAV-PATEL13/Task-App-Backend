from fastapi import HTTPException, Request, status, Depends
from jwt import InvalidTokenError

from sqlalchemy.orm import Session

from src.user.models import UserModel
from src.utils.settings import settings
from src.utils.db import get_db

import jwt

# token send


def is_authenticated(request: Request, db: Session = Depends(get_db)):

    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="You are Unauthorized"
            )

        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)

        user_id = data.get("_id")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="You are Unauthorized"
            )

        return user
    
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="You are Unauthorized"
        )
