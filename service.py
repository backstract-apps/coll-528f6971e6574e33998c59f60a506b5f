from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_books(db: Session):

    query = db.query(models.Books)

    books_all = query.all()
    books_all = (
        [new_data.to_dict() for new_data in books_all] if books_all else books_all
    )
    res = {
        "books_all": books_all,
    }
    return res


async def post_patrons(db: Session, raw_data: schemas.PostPatrons):
    patron_id: int = raw_data.patron_id
    name: str = raw_data.name
    student_id: str = raw_data.student_id
    contact_information: str = raw_data.contact_information
    grade_level: str = raw_data.grade_level

    record_to_be_added = {
        "name": name,
        "patron_id": patron_id,
        "student_id": student_id,
        "grade_level": grade_level,
        "contact_information": contact_information,
    }
    new_patrons = models.Patrons(**record_to_be_added)
    db.add(new_patrons)
    db.commit()
    db.refresh(new_patrons)
    patrons_inserted_record = new_patrons.to_dict()

    res = {
        "patrons_inserted_record": patrons_inserted_record,
    }
    return res


async def put_patrons_patron_id(
    db: Session,
    patron_id: int,
    name: str,
    student_id: str,
    contact_information: str,
    grade_level: str,
):

    query = db.query(models.Patrons)
    query = query.filter(and_(models.Patrons.patron_id == patron_id))
    patrons_edited_record = query.first()

    if patrons_edited_record:
        for key, value in {
            "name": name,
            "patron_id": patron_id,
            "student_id": student_id,
            "grade_level": grade_level,
            "contact_information": contact_information,
        }.items():
            setattr(patrons_edited_record, key, value)

        db.commit()
        db.refresh(patrons_edited_record)

        patrons_edited_record = (
            patrons_edited_record.to_dict()
            if hasattr(patrons_edited_record, "to_dict")
            else vars(patrons_edited_record)
        )
    res = {
        "patrons_edited_record": patrons_edited_record,
    }
    return res


async def delete_patrons_patron_id(db: Session, patron_id: int):

    query = db.query(models.Patrons)
    query = query.filter(and_(models.Patrons.patron_id == patron_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        patrons_deleted = record_to_delete.to_dict()
    else:
        patrons_deleted = record_to_delete
    res = {
        "patrons_deleted": patrons_deleted,
    }
    return res


async def get_loans(db: Session):

    query = db.query(models.Loans)

    loans_all = query.all()
    loans_all = (
        [new_data.to_dict() for new_data in loans_all] if loans_all else loans_all
    )
    res = {
        "loans_all": loans_all,
    }
    return res


async def get_loans_loan_id(db: Session, loan_id: int):

    query = db.query(models.Loans)
    query = query.filter(and_(models.Loans.loan_id == loan_id))

    loans_one = query.first()

    loans_one = (
        (loans_one.to_dict() if hasattr(loans_one, "to_dict") else vars(loans_one))
        if loans_one
        else loans_one
    )

    res = {
        "loans_one": loans_one,
    }
    return res


async def post_loans(db: Session, raw_data: schemas.PostLoans):
    loan_id: int = raw_data.loan_id
    book_id: int = raw_data.book_id
    patron_id: int = raw_data.patron_id
    borrowed_date: str = raw_data.borrowed_date
    due_date: str = raw_data.due_date

    record_to_be_added = {
        "book_id": book_id,
        "loan_id": loan_id,
        "due_date": due_date,
        "patron_id": patron_id,
        "borrowed_date": borrowed_date,
    }
    new_loans = models.Loans(**record_to_be_added)
    db.add(new_loans)
    db.commit()
    db.refresh(new_loans)
    loans_inserted_record = new_loans.to_dict()

    res = {
        "loans_inserted_record": loans_inserted_record,
    }
    return res


async def get_books_book_id(db: Session, book_id: int):

    query = db.query(models.Books)
    query = query.filter(and_(models.Books.book_id == book_id))

    books_one = query.first()

    books_one = (
        (books_one.to_dict() if hasattr(books_one, "to_dict") else vars(books_one))
        if books_one
        else books_one
    )

    res = {
        "books_one": books_one,
    }
    return res


async def post_books(db: Session, raw_data: schemas.PostBooks):
    book_id: int = raw_data.book_id
    title: str = raw_data.title
    author: str = raw_data.author
    isbn: str = raw_data.isbn
    publication_date: datetime.date = raw_data.publication_date
    category_id: int = raw_data.category_id

    record_to_be_added = {
        "isbn": isbn,
        "title": title,
        "author": author,
        "book_id": book_id,
        "category_id": category_id,
        "publication_date": publication_date,
    }
    new_books = models.Books(**record_to_be_added)
    db.add(new_books)
    db.commit()
    db.refresh(new_books)
    books_inserted_record = new_books.to_dict()

    res = {
        "books_inserted_record": books_inserted_record,
    }
    return res


async def put_books_book_id(
    db: Session,
    book_id: int,
    title: str,
    author: str,
    isbn: str,
    publication_date: str,
    category_id: int,
):

    query = db.query(models.Books)
    query = query.filter(and_(models.Books.book_id == book_id))
    books_edited_record = query.first()

    if books_edited_record:
        for key, value in {
            "isbn": isbn,
            "title": title,
            "author": author,
            "book_id": book_id,
            "category_id": category_id,
            "publication_date": publication_date,
        }.items():
            setattr(books_edited_record, key, value)

        db.commit()
        db.refresh(books_edited_record)

        books_edited_record = (
            books_edited_record.to_dict()
            if hasattr(books_edited_record, "to_dict")
            else vars(books_edited_record)
        )
    res = {
        "books_edited_record": books_edited_record,
    }
    return res


async def delete_books_book_id(db: Session, book_id: int):

    query = db.query(models.Books)
    query = query.filter(and_(models.Books.book_id == book_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        books_deleted = record_to_delete.to_dict()
    else:
        books_deleted = record_to_delete
    res = {
        "books_deleted": books_deleted,
    }
    return res


async def get_patrons(db: Session):

    query = db.query(models.Patrons)

    patrons_all = query.all()
    patrons_all = (
        [new_data.to_dict() for new_data in patrons_all] if patrons_all else patrons_all
    )
    res = {
        "patrons_all": patrons_all,
    }
    return res


async def get_patrons_patron_id(db: Session, patron_id: int):

    query = db.query(models.Patrons)
    query = query.filter(and_(models.Patrons.patron_id == patron_id))

    patrons_one = query.first()

    patrons_one = (
        (
            patrons_one.to_dict()
            if hasattr(patrons_one, "to_dict")
            else vars(patrons_one)
        )
        if patrons_one
        else patrons_one
    )

    res = {
        "patrons_one": patrons_one,
    }
    return res


async def put_loans_loan_id(
    db: Session,
    loan_id: int,
    book_id: int,
    patron_id: int,
    borrowed_date: str,
    due_date: str,
):

    query = db.query(models.Loans)
    query = query.filter(and_(models.Loans.loan_id == loan_id))
    loans_edited_record = query.first()

    if loans_edited_record:
        for key, value in {
            "book_id": book_id,
            "loan_id": loan_id,
            "due_date": due_date,
            "patron_id": patron_id,
            "borrowed_date": borrowed_date,
        }.items():
            setattr(loans_edited_record, key, value)

        db.commit()
        db.refresh(loans_edited_record)

        loans_edited_record = (
            loans_edited_record.to_dict()
            if hasattr(loans_edited_record, "to_dict")
            else vars(loans_edited_record)
        )
    res = {
        "loans_edited_record": loans_edited_record,
    }
    return res


async def delete_loans_loan_id(db: Session, loan_id: int):

    query = db.query(models.Loans)
    query = query.filter(and_(models.Loans.loan_id == loan_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        loans_deleted = record_to_delete.to_dict()
    else:
        loans_deleted = record_to_delete
    res = {
        "loans_deleted": loans_deleted,
    }
    return res


async def get_categories(db: Session):

    query = db.query(models.Categories)

    categories_all = query.all()
    categories_all = (
        [new_data.to_dict() for new_data in categories_all]
        if categories_all
        else categories_all
    )
    res = {
        "categories_all": categories_all,
    }
    return res


async def get_categories_category_id(db: Session, category_id: int):

    query = db.query(models.Categories)
    query = query.filter(and_(models.Categories.category_id == category_id))

    categories_one = query.first()

    categories_one = (
        (
            categories_one.to_dict()
            if hasattr(categories_one, "to_dict")
            else vars(categories_one)
        )
        if categories_one
        else categories_one
    )

    res = {
        "categories_one": categories_one,
    }
    return res


async def post_categories(db: Session, raw_data: schemas.PostCategories):
    category_id: int = raw_data.category_id
    name: str = raw_data.name

    record_to_be_added = {"name": name, "category_id": category_id}
    new_categories = models.Categories(**record_to_be_added)
    db.add(new_categories)
    db.commit()
    db.refresh(new_categories)
    categories_inserted_record = new_categories.to_dict()

    res = {
        "categories_inserted_record": categories_inserted_record,
    }
    return res


async def put_categories_category_id(db: Session, category_id: int, name: str):

    query = db.query(models.Categories)
    query = query.filter(and_(models.Categories.category_id == category_id))
    categories_edited_record = query.first()

    if categories_edited_record:
        for key, value in {"name": name, "category_id": category_id}.items():
            setattr(categories_edited_record, key, value)

        db.commit()
        db.refresh(categories_edited_record)

        categories_edited_record = (
            categories_edited_record.to_dict()
            if hasattr(categories_edited_record, "to_dict")
            else vars(categories_edited_record)
        )
    res = {
        "categories_edited_record": categories_edited_record,
    }
    return res


async def delete_categories_category_id(db: Session, category_id: int):

    query = db.query(models.Categories)
    query = query.filter(and_(models.Categories.category_id == category_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        categories_deleted = record_to_delete.to_dict()
    else:
        categories_deleted = record_to_delete
    res = {
        "categories_deleted": categories_deleted,
    }
    return res
