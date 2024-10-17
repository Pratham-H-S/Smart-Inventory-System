# backend/app/schemas/supplier.py

from pydantic import BaseModel

class SupplierBase(BaseModel):
    name: str
    contact_email: str
    contact_phone: str | None = None

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    name: str | None = None
    contact_email: str | None = None
    contact_phone: str | None = None

class SupplierOut(SupplierBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
