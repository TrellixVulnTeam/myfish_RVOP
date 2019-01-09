import json
from sqlalchemy import Column, String, Integer
from app.model.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    tittle = Column(String(60), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def add_to_current_upload(book):
        book_detail = json.loads(book).get('book')
        print(book_detail)
