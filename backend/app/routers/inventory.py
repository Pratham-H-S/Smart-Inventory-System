# backend/app/routers/inventory.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from dependencies.auth import get_current_active_user, get_current_active_admin
from dependencies.auth import get_db

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)

@router.post("/", response_model=schemas.InventoryOut)
def create_inventory(item: schemas.InventoryCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if current_user.role not in ["admin", "inventory_manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_item = models.InventoryItem(**item.dict(), owner_id=current_user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[schemas.InventoryOut])
def read_inventory(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    items = db.query(models.InventoryItem).offset(skip).limit(limit).all()
    return items

@router.get("/{item_id}", response_model=schemas.InventoryOut)
def read_inventory_item(item_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    item = db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=schemas.InventoryOut)
def update_inventory_item(item_id: int, item: schemas.InventoryUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if current_user.role not in ["admin", "inventory_manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_item = db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{item_id}")
def delete_inventory_item(item_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_admin)):
    db_item = db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"detail": "Item deleted"}
