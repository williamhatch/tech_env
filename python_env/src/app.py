#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FastAPI application for interview environment
"""

from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .database import get_db, engine
from . import models

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Interview API",
    description="FastAPI application for technical interviews",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for request/response
class ItemBase(BaseModel):
    """Base Item schema"""
    name: str
    description: Optional[str] = None
    is_active: bool = True


class ItemCreate(ItemBase):
    """Item creation schema"""
    pass


class ItemResponse(ItemBase):
    """Item response schema"""
    id: int
    created_at: str
    updated_at: Optional[str] = None

    class Config:
        orm_mode = True


@app.get("/")
def read_root():
    """
    Root endpoint
    
    Returns:
        dict: Welcome message
    """
    return {"message": "Welcome to the Interview API"}


@app.get("/items/", response_model=List[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all items
    
    Args:
        skip: Number of items to skip
        limit: Maximum number of items to return
        db: Database session
        
    Returns:
        List[Item]: List of items
    """
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items


@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item
    
    Args:
        item: Item data
        db: Database session
        
    Returns:
        Item: Created item
    """
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get item by ID
    
    Args:
        item_id: Item ID
        db: Database session
        
    Returns:
        Item: Item with the specified ID
        
    Raises:
        HTTPException: If item not found
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete item by ID
    
    Args:
        item_id: Item ID
        db: Database session
        
    Raises:
        HTTPException: If item not found
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return None
