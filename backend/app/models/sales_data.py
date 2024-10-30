# backend/app/models/sales_data.py

from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class SalesData(Base):
    __tablename__ = "sales_data"

    id = Column(Integer, primary_key=True, index=True)
    inventory_item_id = Column(Integer, ForeignKey("inventory_items.id"))
    sale_date = Column(Date, nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    total_sale_value = Column(Float, nullable=False)

    inventory_item = relationship("InventoryItem", back_populates="sales")
