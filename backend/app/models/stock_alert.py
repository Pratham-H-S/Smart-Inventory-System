# backend/app/models/stock_alert.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class StockAlert(Base):
    __tablename__ = "stock_alert"

    id = Column(Integer, primary_key=True, index=True)
    inventory_item_id = Column(Integer, ForeignKey("inventory_items.id"), nullable=False)
    alert_date = Column(Date, nullable=False)
    alert_type = Column(String(50), nullable=False)

    inventory_item = relationship("InventoryItem", back_populates="stock_alerts")
