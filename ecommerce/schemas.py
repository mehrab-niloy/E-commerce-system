from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    category_id: int

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int

class CartResponse(BaseModel):
    id: int
    items: List[CartItemCreate]
    total_price: float

class OrderCreate(BaseModel):
    cart_id: int