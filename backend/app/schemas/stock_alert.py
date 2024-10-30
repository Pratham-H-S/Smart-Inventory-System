# backend/app/schemas/stock_alert.py

from pydantic import BaseModel
from datetime import date

class StockAlertBase(BaseModel):
    inventory_item_id: int
    alert_date: date
    alert_type: str

class StockAlertCreate(StockAlertBase):
    pass

class StockAlertOut(StockAlertBase):
    id: int

    class Config:
        orm_mode = True
