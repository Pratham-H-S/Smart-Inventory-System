# backend/app/main.py
from fastapi import FastAPI
import sys
print("--------------------------------")
print(sys.path)
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from routers import auth, users, inventory, suppliers  # Use absolute imports
from app.database import engine, Base
from app.utils.logger import logger
# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Inventory Management System",
    description="A web application to manage inventory efficiently.",
    version="1.0.0",
)

# Include all routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(inventory.router)
app.include_router(suppliers.router)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to the Smart Inventory Management System API"}