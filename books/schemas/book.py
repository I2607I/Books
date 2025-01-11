from typing import List, Literal
from datetime import date
from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    name: str | None = None
    author: str | None = None
    category: str | None = None
    original_language: str | None = None
    writing_year: int | None = None
    word_count: int | None = None
    read_at: date | None = None

    class Config:
        from_attributes = True


# class ProductWithTimeSchema(ProductSchema):
#     id: int
#     created_at: datetime
#     updated_at: datetime

# class ProductsSchema(BaseModel):
#     items: List[ProductWithTimeSchema]
#     total: int
#     page: int
#     per_page: int
#     pages: int

#     class Config:
#         from_attributes = True
