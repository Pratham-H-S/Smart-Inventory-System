from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from typing import List
from app import models, schemas
from app.models import sales_data, stock_alert
from dependencies.auth import get_db

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

@router.get("/stock-alerts-history", response_model=List[schemas.StockAlertOut])
def get_stock_alerts_history(start_date: date, end_date: date, db: Session = Depends(get_db)):
    alerts = db.query(stock_alert.StockAlert).filter(
        stock_alert.StockAlert.alert_date >= start_date, 
        stock_alert.StockAlert.alert_date <= end_date
    ).all()
    return alerts

@router.get("/sales-vs-inventory", response_model=List[schemas.SalesDataOut])
def get_sales_vs_inventory(start_date: date, end_date: date, db: Session = Depends(get_db)):
    sale_data = db.query(
        sales_data.SalesData.sale_date,
        sales_data.SalesData.quantity_sold,
        sales_data.SalesData.total_sale_value,
        models.inventory.InventoryItem.quantity.label("inventory_level")
    ).filter(
        sales_data.SalesData.sale_date >= start_date, 
        sales_data.SalesData.sale_date <= end_date
    ).join(models.inventory.InventoryItem, sales_data.SalesData.inventory_item_id == models.inventory.InventoryItem.id).all()

    result = []
    for sale in sale_data:
        result.append({
            "sale_date": sale.sale_date,
            "quantity_sold": sale.quantity_sold,
            "total_sale_value": sale.total_sale_value,
            "inventory_level": sale.inventory_level
        })

    return result

@router.get("/supplier-performance", response_model=List[schemas.SupplierOut])
def get_supplier_performance(start_date: date, end_date: date, db: Session = Depends(get_db)):
    suppliers = db.query(models.Supplier).join(models.InventoryItem).join(sales_data.SalesData).filter(
        sales_data.SalesData.sale_date >= start_date, 
        sales_data.SalesData.sale_date <= end_date
    ).all()
    return suppliers
