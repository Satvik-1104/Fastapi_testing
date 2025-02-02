from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models


def get_all(db: Session):
    return db.query(models.Blog).all()


def get_blog(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the ID {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
    return blog


def make_blog(request: schemas.BlogBase, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=3)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def remove_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "Deletion Successful"


def update_blog(id: int, request: schemas.BlogBase, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog of id {id} not found")
    for key, value in request.model_dump().items():
        setattr(blog, key, value)
    db.commit()
    return "updated"
