from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Books(Base):
    __tablename__ = 'books'
    book_id = Column(String, primary_key=True)
    title = Column(String, primary_key=False)
    author = Column(String, primary_key=False)
    isbn = Column(String, primary_key=False)
    publication_date = Column(Date, primary_key=False)
    category_id = Column(Integer, primary_key=False)


class Patrons(Base):
    __tablename__ = 'patrons'
    patron_id = Column(String, primary_key=True)
    name = Column(String, primary_key=False)
    student_id = Column(String, primary_key=False)
    contact_information = Column(String, primary_key=False)
    grade_level = Column(String, primary_key=False)


class Loans(Base):
    __tablename__ = 'loans'
    loan_id = Column(String, primary_key=True)
    book_id = Column(Integer, primary_key=False)
    patron_id = Column(Integer, primary_key=False)
    borrowed_date = Column(String, primary_key=False)
    due_date = Column(String, primary_key=False)


class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(String, primary_key=True)
    name = Column(String, primary_key=False)


