# HomeServe – Complete Starter Project

This is a runnable MVP starter for the HomeServe home-services booking SaaS.
It contains a FastAPI + SQLAlchemy backend and a React + Vite frontend.

## Important
- This is a clean starter package; it does not overwrite your existing `backend` folder.
- It implements the core MVP workflows and creates the 20 database tables.
- Razorpay and Cloudinary are provided as integration-ready placeholders. Add real credentials and verify webhooks before production.
- Review and migrate your existing database before using this package against it. The SQLAlchemy models here are a coherent baseline based on the table names and fields discussed, not a byte-for-byte copy of every existing model you created.
- Do not deploy with the development SECRET_KEY or default admin credentials.

## Requirements
- Python 3.11+
- Node.js 20+
- MySQL / XAMPP

## Backend setup (Windows PowerShell)
1. Create a MySQL database named `homeserve_db` in SQLyog.
2. Open the `backend` folder:
   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   copy .env.example .env
   ```
3. Edit `.env` and set `DATABASE_URL` for your MySQL user/password.
4. Create tables and seed a development admin:
   ```powershell
   python -m app.seed
   ```
5. Start API:
   ```powershell
   uvicorn app.main:app --reload
   ```
6. Swagger: http://127.0.0.1:8000/docs

Development admin after seeding:
- Email: `admin@homeserve.local`
- Password: `ChangeMe123!`
Change it immediately and never use this account in production.

## Frontend setup
Open a second terminal:
```powershell
cd frontend
npm install
copy .env.example .env
npm run dev
```
Open the Vite URL shown in the terminal (normally http://localhost:5173).

## MVP endpoints
- `/auth/register`, `/auth/login`
- `/users/me`
- `/categories` (public active list; admin CRUD)
- `/services` (public list; admin CRUD)
- `/addresses` (customer CRUD)
- `/providers/me` and `/providers/services`
- `/availability`
- `/bookings` (customer create/list; provider/admin status update)
- `/payments` (test-mode placeholder record)
- `/reviews`
- `/coupons`
- `/complaints`
- `/notifications`
- `/invoices`
- `/admin/dashboard`

## Production checklist
Use Alembic migrations, strong secrets, HTTPS, email/SMS verification, rate limiting,
audit logs, payment-provider signature verification, object storage, backups, automated
tests, and role/ownership authorization review before launch.
