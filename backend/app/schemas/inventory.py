# backend/app/schemas/inventory.py

from pydantic import BaseModel

class InventoryBase(BaseModel):
    name: str
    quantity: int
    price: float
    supplier_id: int

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(BaseModel):
    name: str | None = None
    quantity: int | None = None
    price: float | None = None
    supplier_id: int | None = None

class InventoryOut(InventoryBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
