from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Order(BaseModel):
    id: Optional[int]
    petId: int
    quantity: int
    shipDate: datetime
    status: str
    complete: bool
