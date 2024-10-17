# backend/app/models/inventory.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="inventory")
    supplier = relationship("Supplier", back_populates="products")
