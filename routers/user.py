from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, oauth2
from ..database import get_db
from ..repository import user

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.make_user(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.req_user(id, db)
