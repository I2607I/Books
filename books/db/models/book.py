from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP, FLOAT, DATE
from sqlalchemy.sql import func

from books.db import DeclarativeBase


class Book(DeclarativeBase):
    __tablename__ = "book"

    id = Column(
        INTEGER,
        primary_key=True,
        autoincrement=True,
        unique=True,
    )
    name = Column(
        TEXT,
        nullable=True,
    )
    author = Column(
        TEXT,
        nullable=True,
    )
    category = Column(
        TEXT,
        nullable=True,
    )
    original_language = Column(
        TEXT,
        nullable=True,
    )
    writing_year = Column(
        INTEGER,
        nullable=True,
    )
    word_count = Column(
        INTEGER,
        nullable=True,
    )
    read_at = Column(
        DATE,
        nullable=True
    )

    def __repr__(self):
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
