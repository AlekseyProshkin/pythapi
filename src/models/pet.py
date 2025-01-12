from pydantic import BaseModel
from typing import List, Optional

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class Pet(BaseModel):
    id: Optional[int]
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: str
