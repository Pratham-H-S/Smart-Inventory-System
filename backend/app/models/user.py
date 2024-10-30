# backend/app/models/user.py

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False)  # Set length as needed
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String(255), nullable=False, default="user")  # Roles: admin, inventory_manager, supplier, user
    inventory = relationship("InventoryItem", primaryjoin="User.id==InventoryItem.owner_id")
    suppliers = relationship("Supplier", back_populates="owner")
