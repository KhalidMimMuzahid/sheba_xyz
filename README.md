<!--   Project Documentation   -->

<!-- create a seperate venv and open this project in this venv

to test:  PYTHONPATH=. pytest -v

docker-compose build
docker-compose up

pip3 install -r requirements.txt
set up database for the user and password with the correct database name
uvicorn main:app --reload -->

# 🛠️ Service Booking FastAPI

A FastAPI–powered backend for user authentication, service management, and booking management.

---

## 📋 Prerequisites

- Internet connection is **required**
- Valid email address (to receive notification emails from Sheba.xyz)
- Python 3.10+
- Git
- PostgreSQL installed on your machine
- Docker Desktop

---

## 🚀 Setup & Run


### 1. Clone the repository

```bash
git clone https://github.com/KhalidMimMuzahid/service_booking_fastapi.git
cd service_booking_fastapi
```

## With Docker

### Ensure `start.sh` is executable
```bash
chmod +x start.sh
```
### Build and start the containers

```bash
docker-compose up --build -d
```
This creates two containers:
- **web** – your FastAPI app, listening on port 8000  
- **db**  – Postgres database, listening on port 5432  

### Verify everything is up

```bash
docker-compose ps
```

### View logs

```bash
docker-compose logs -f web
```

Look for:

```
✅ Postgres is up – starting FastAPI...
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Stopping & Cleaning Up

- Stop and remove containers & network:
  ```bash
  docker-compose down
  ```
- Remove volumes (data will be lost):
  ```bash
  docker-compose down -v
  ```

## With Your Local Machine
### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Update the `.env` file in the project root with your PostgreSQL and email credentials:

```env
DB_USER=postgres
DB_PASS=test1234
DB_NAME=sheba_xyz
DB_PORT=5432
DB_HOST=db
SENDER_PASSWORD=ysnc qcsv ybmy lnlb
JWT_ALGORITHM=HS256
JWT_SECRET=secret_key
```

> ⚠️ Ensure PostgreSQL is running and update the `.env` credentials according to your machine setup.

### 5. Run the app

```bash
uvicorn app.main:app --reload
```

If the above doesn’t work, try:

```bash
PYTHONPATH=. uvicorn app.main:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 6. Interactive API Docs

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 How to Run Tests

1. Install test dependencies:

```bash
pip install pytest pytest-asyncio httpx
```

2. Run tests:

```bash
PYTHONPATH=. pytest -v
```

> ✅ Tests use an in-memory SQLite database—no additional setup required.

---

## 📦 Modules Overview

### 🔐 USER

- **Register**: User signs up with a valid email → receives confirmation email.
- **Login**: Receive access token via email and password.
- **Auth**: Bearer token required for accessing protected admin APIs.
- Passwords are hashed before storage.

---

### 🧾 SERVICE

- **Add Service** (admin API):  
  Name must be **unique**
- **Get Services** (public API):  
  - Paginated  
  - Filter by category
- **Delete Service** (admin API):  
  Delete by service ID
- **Update Service** (admin API):  
  Update multiple fields by service ID

---

### 📅 BOOKING

- **Book a Service** (public API):  
  Must provide valid email → confirmation sent
- **Get Bookings** (admin API):  
  Paginated list of all bookings
- **Check Booking Status** (public API):  
  Check by booking ID
- **Update Booking Status** (admin API):  
  Status (Enum with 6 values), default is `pending`  
  Updates trigger email notification to user

---

## 📄 Pagination

Pagination data is available in `meta_data` object:
- `current_page`: Current page number
- `limit`: Items per page
- `total_page`: Total number of pages
- `previous_page`: `current_page - 1` (if not first)
- `next_page`: `current_page + 1` (if not last)

---

## 🔒 Access Control

- **Public Access**:
  - Register
  - Login
  - List services
  - Create bookings
  - Check booking status

- **Authenticated Access (Bearer Token Required)**:
  - Add, update, delete services
  - View all bookings

---

## 🧪 Test Environment

Tests run against a fresh **in-memory SQLite** database.


---

## ✅ Assumptions

### 📧 Email Notifications
- Email may go to the client’s **spam folder**
- Emails **may take time** to arrive