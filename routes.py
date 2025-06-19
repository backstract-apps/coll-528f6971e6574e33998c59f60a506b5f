from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/books/')
async def get_books(db: Session = Depends(get_db)):
    try:
        return await service.get_books(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/patrons/')
async def post_patrons(raw_data: schemas.PostPatrons, db: Session = Depends(get_db)):
    try:
        return await service.post_patrons(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/patrons/patron_id/')
async def put_patrons_patron_id(patron_id: int, name: Annotated[str, Query(max_length=100)], student_id: Annotated[str, Query(max_length=100)], contact_information: Annotated[str, Query(max_length=100)], grade_level: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_patrons_patron_id(db, patron_id, name, student_id, contact_information, grade_level)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/patrons/patron_id')
async def delete_patrons_patron_id(patron_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_patrons_patron_id(db, patron_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/loans/')
async def get_loans(db: Session = Depends(get_db)):
    try:
        return await service.get_loans(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/loans/loan_id')
async def get_loans_loan_id(loan_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_loans_loan_id(db, loan_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/loans/')
async def post_loans(raw_data: schemas.PostLoans, db: Session = Depends(get_db)):
    try:
        return await service.post_loans(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/books/book_id')
async def get_books_book_id(book_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_books_book_id(db, book_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/books/')
async def post_books(raw_data: schemas.PostBooks, db: Session = Depends(get_db)):
    try:
        return await service.post_books(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/books/book_id/')
async def put_books_book_id(book_id: int, title: Annotated[str, Query(max_length=100)], author: Annotated[str, Query(max_length=100)], isbn: Annotated[str, Query(max_length=100)], publication_date: str, category_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_books_book_id(db, book_id, title, author, isbn, publication_date, category_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/books/book_id')
async def delete_books_book_id(book_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_books_book_id(db, book_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/patrons/')
async def get_patrons(db: Session = Depends(get_db)):
    try:
        return await service.get_patrons(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/patrons/patron_id')
async def get_patrons_patron_id(patron_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_patrons_patron_id(db, patron_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/loans/loan_id/')
async def put_loans_loan_id(loan_id: int, book_id: int, patron_id: int, borrowed_date: Annotated[str, Query(max_length=100)], due_date: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_loans_loan_id(db, loan_id, book_id, patron_id, borrowed_date, due_date)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/loans/loan_id')
async def delete_loans_loan_id(loan_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_loans_loan_id(db, loan_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/categories/')
async def get_categories(db: Session = Depends(get_db)):
    try:
        return await service.get_categories(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/categories/category_id')
async def get_categories_category_id(category_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_categories_category_id(db, category_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/categories/')
async def post_categories(raw_data: schemas.PostCategories, db: Session = Depends(get_db)):
    try:
        return await service.post_categories(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/categories/category_id/')
async def put_categories_category_id(category_id: int, name: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_categories_category_id(db, category_id, name)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/categories/category_id')
async def delete_categories_category_id(category_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_categories_category_id(db, category_id)
    except Exception as e:
        raise HTTPException(500, str(e))

