from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..hash_passwords import Hash


def make_user(request: schemas.User, db: Session):
    new_user = models.User(name=request.name,
                           username=request.username,
                           password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def req_user(id: int, db: Session):
    this_user = db.query(models.User).filter(models.User.id == id).first()
    if not this_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There is not user with id {id}")
    return this_user
