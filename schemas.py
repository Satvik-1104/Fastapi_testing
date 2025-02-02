from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str


class BlogResponse(BlogBase):
    id: int

    class Config:
        from_attributes = True


class User(BaseModel):
    name: str
    username: str
    password: str


class BlogTitleBody(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True


class ShowUser(BaseModel):
    name: str
    username: str
    blogs: List[BlogTitleBody] = []

    class Config:
        from_attributes = True


class BlogTitleBodyCreator(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
