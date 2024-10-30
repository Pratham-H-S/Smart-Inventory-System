# backend/app/schemas/sales_data.py

from pydantic import BaseModel
from datetime import date

class SalesDataBase(BaseModel):
    inventory_item_id: int
    sale_date: date
    quantity_sold: int
    total_sale_value: float

class SalesDataCreate(SalesDataBase):
    pass

class SalesDataOut(BaseModel):
    id: int
    inventory_item_id: int
    quantity_sold: int
    total_sale_value: float
    sale_date: date

    class Config:
        orm_mode = True
