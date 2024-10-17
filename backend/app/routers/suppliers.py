# backend/app/routers/suppliers.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from dependencies.auth import get_current_active_user, get_current_active_admin
from dependencies.auth import get_db

router = APIRouter(
    prefix="/suppliers",
    tags=["suppliers"]
)

@router.post("/", response_model=schemas.SupplierOut)
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if current_user.role not in ["admin", "supplier"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_supplier = models.Supplier(**supplier.dict(), owner_id=current_user.id)
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@router.get("/", response_model=List[schemas.SupplierOut])
def read_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if current_user.role == "supplier":
        suppliers = db.query(models.Supplier).filter(models.Supplier.owner_id == current_user.id).offset(skip).limit(limit).all()
    else:
        suppliers = db.query(models.Supplier).offset(skip).limit(limit).all()
    return suppliers

@router.put("/{supplier_id}", response_model=schemas.SupplierOut)
def update_supplier(supplier_id: int, supplier: schemas.SupplierUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    if current_user.role != "admin" and db_supplier.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    for key, value in supplier.dict(exclude_unset=True).items():
        setattr(db_supplier, key, value)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@router.delete("/{supplier_id}")
def delete_supplier(supplier_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_admin)):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    db.delete(db_supplier)
    db.commit()
    return {"detail": "Supplier deleted"}
