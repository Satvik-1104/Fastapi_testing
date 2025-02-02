from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from .. import schemas, oauth2
from ..database import get_db
from ..repository import blog


router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get("/", response_model=list[schemas.BlogResponse])  # Gets all the Blogs in the blogs table
def all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get("/{id}", status_code=200, response_model=schemas.BlogTitleBodyCreator)  # Gets the Blogs of specific id from the blogs table
def get_specific_blog(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blog(db, id)


@router.post("/", status_code=status.HTTP_201_CREATED)  # To create a blog in the blogs table
def create_blog(request: schemas.BlogBase, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.make_blog(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)  # To delete a blog from the blogs table
def delete_id_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.remove_blog(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)  # to update a blog in the blogs table
def update_id_blog(id: int, request: schemas.BlogBase, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)
