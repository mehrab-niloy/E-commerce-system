# E-commerce-system
# 🛒 FastAPI E-Commerce API

A simple e-commerce backend built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. This API includes user authentication (JWT), product and category management, shopping cart functionality, and order processing.

---

## 🚀 Features
- **User Authentication** (JWT-based Login, Registration, Logout, Protected Endpoints)
- **Product & Category Management** (CRUD Operations, Filtering, Pagination)
- **Shopping Cart System** (Add, Update, Remove Items)
- **Order Management** (Checkout, Stock Deduction)

---

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy


---

## 📂 Project Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/ecommerce-fastapi.git
cd ecommerce-fastapi
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file and add the following details:
```ini
DATABASE_URL=postgresql://youruser:yourpassword@localhost/ecommerce_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5️⃣ Run Database Migrations
```sh
alembic upgrade head
```

### 6️⃣ Start the FastAPI Server
```sh
uvicorn main:app --reload
```

Server runs at: **http://127.0.0.1:8000**

API Documentation:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

##  API Endpoints



| Method | Endpoint        | Description               |
|--------|----------------|---------------------------|
| POST    | /register      |User registration |
| POST    | /login |user login       |
| POST   | /products      | Create a product (Admin)  |
| GET    | /products | Get products  |
| POST | /cart |Add cart items  |
| POST    | /orders    | place orders        |




---

