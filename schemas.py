from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Books(BaseModel):
    book_id: Any
    title: str
    author: str
    isbn: str
    publication_date: datetime.date
    category_id: int


class ReadBooks(BaseModel):
    book_id: Any
    title: str
    author: str
    isbn: str
    publication_date: datetime.date
    category_id: int
    class Config:
        from_attributes = True


class Patrons(BaseModel):
    patron_id: Any
    name: str
    student_id: str
    contact_information: str
    grade_level: str


class ReadPatrons(BaseModel):
    patron_id: Any
    name: str
    student_id: str
    contact_information: str
    grade_level: str
    class Config:
        from_attributes = True


class Loans(BaseModel):
    loan_id: Any
    book_id: int
    patron_id: int
    borrowed_date: Any
    due_date: Any


class ReadLoans(BaseModel):
    loan_id: Any
    book_id: int
    patron_id: int
    borrowed_date: Any
    due_date: Any
    class Config:
        from_attributes = True


class Categories(BaseModel):
    category_id: Any
    name: str


class ReadCategories(BaseModel):
    category_id: Any
    name: str
    class Config:
        from_attributes = True




class PostPatrons(BaseModel):
    patron_id: int = Field(...)
    name: str = Field(..., max_length=100)
    student_id: str = Field(..., max_length=100)
    contact_information: str = Field(..., max_length=100)
    grade_level: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostLoans(BaseModel):
    loan_id: int = Field(...)
    book_id: int = Field(...)
    patron_id: int = Field(...)
    borrowed_date: str = Field(..., max_length=100)
    due_date: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostBooks(BaseModel):
    book_id: int = Field(...)
    title: str = Field(..., max_length=100)
    author: str = Field(..., max_length=100)
    isbn: str = Field(..., max_length=100)
    publication_date: Any = Field(...)
    category_id: int = Field(...)

    class Config:
        from_attributes = True



class PostCategories(BaseModel):
    category_id: int = Field(...)
    name: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

