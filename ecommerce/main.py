from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User  # Import the User model here
from schemas import UserCreate, UserLogin, ProductCreate, CartItemCreate, OrderCreate
from crud import create_user, get_user_by_email, create_product, get_products, add_to_cart, create_order
from auth import get_password_hash, verify_password, create_access_token, get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/products")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

@app.get("/products")
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_products(db=db, skip=skip, limit=limit)

@app.post("/cart")
def add_cart_item(item: CartItemCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return add_to_cart(db=db, cart_id=user.carts[0].id, item=item)

@app.post("/orders")
def place_order(order: OrderCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_order(db=db, order=order)