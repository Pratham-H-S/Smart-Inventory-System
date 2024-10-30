from pydantic import BaseModel
from datetime import date
from typing import Optional  # Import Optional for nullable types

class InventoryBase(BaseModel):
    name: str
    quantity: int
    price: float
    supplier_id: int
    date: date

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    supplier_id: Optional[int] = None
    date: Optional[date] = None

class InventoryOut(InventoryBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
