from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    supplier = relationship("Supplier", back_populates="products")
    owner = relationship("User", back_populates="inventory")
    sales = relationship("SalesData", back_populates="inventory_item")
    stock_alerts = relationship("StockAlert", back_populates="inventory_item")