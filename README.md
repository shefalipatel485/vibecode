
# HomeServe – Home Services Booking SaaS Platform

## 1. Project Overview

**HomeServe** is a web-based Home Services Booking SaaS Platform that connects customers with professional home service providers and technicians.

The platform allows customers to discover services, view service details, book appointments, manage addresses, make payments, and submit reviews.

Service providers can manage their services, availability, and bookings, while technicians can manage their assigned jobs. Administrators can manage users, service categories, bookings, and platform activities.

The main objective of HomeServe is to simplify home service management through a centralized, secure, and user-friendly platform.

## 2. Project Objectives

- Provide an online platform for booking home services.
- Connect customers with verified service providers.
- Allow service providers to manage their services and availability.
- Enable technicians to manage assigned service requests.
- Provide secure user authentication and role-based authorization.
- Manage bookings, payments, invoices, and reviews.
- Maintain customer and service provider information.
- Provide administrative control over platform activities.

## 3. Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React.js |
| Frontend Build Tool | Vite |
| Styling | CSS / Tailwind CSS (as implemented) |
| Backend | Python FastAPI |
| Programming Language | Python |
| Database | MySQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Password Security | Passlib / bcrypt |
| API Testing | Postman |
| Automated Testing | Pytest / Playwright |
| Version Control | Git and GitHub |
| Payment Integration | Razorpay Test Mode (planned integration) |
| Image Storage | Cloudinary (planned integration) |
| Frontend Deployment | Vercel |
| Backend Deployment | Render |

## 4. User Roles

### 4.1 Super Admin
- Manage platform users.
- Manage customers and service providers.
- Manage service categories and services.
- Monitor bookings and payments.
- Manage complaints and platform notifications.
- View overall platform activities.

### 4.2 Customer
- Register and log in.
- Manage personal profile.
- Add and manage addresses.
- Browse service categories.
- View available services.
- Create service bookings.
- Track booking information.
- View payment and invoice details.
- Submit reviews and complaints.

### 4.3 Service Provider
- Register as a service provider.
- Manage business profile.
- Manage offered services.
- Manage service areas.
- Set availability slots.
- View booking requests.
- Manage technicians.
- Track provider earnings.

### 4.4 Technician
- Access assigned jobs.
- View booking details.
- Manage job availability.
- Update assigned service progress (where implemented).

## 5. Main Project Modules

1. User Authentication and Authorization
2. Customer Management
3. Service Provider Management
4. Technician Management
5. Address Management
6. Service Category Management
7. Service Management
8. Provider Service Management
9. Service Area Management
10. Availability Management
11. Booking Management
12. Booking Assignment Management
13. Booking Image Management
14. Payment Management
15. Invoice Management
16. Coupon Management
17. Review Management
18. Complaint Management
19. Notification Management
20. Provider Earnings Management

## 6. Database Design

The project uses MySQL as its relational database and SQLAlchemy as its ORM.

### Database Name

`homeserve_db`

### Database Tables

| No. | Table Name | Description |
|---|---|---|
| 1 | users | Stores login and user information |
| 2 | customers | Stores customer profile information |
| 3 | service_providers | Stores provider business information |
| 4 | technicians | Stores technician details |
| 5 | addresses | Stores customer service addresses |
| 6 | service_categories | Stores service categories |
| 7 | services | Stores individual services |
| 8 | provider_services | Maps providers to services |
| 9 | service_areas | Stores provider service locations |
| 10 | availability_slots | Stores provider availability |
| 11 | bookings | Stores customer service bookings |
| 12 | booking_assignments | Maps bookings to technicians |
| 13 | booking_images | Stores booking-related image references |
| 14 | payments | Stores payment transaction details |
| 15 | invoices | Stores invoice information |
| 16 | coupons | Stores discount coupon information |
| 17 | reviews | Stores customer reviews |
| 18 | complaints | Stores customer complaints |
| 19 | notifications | Stores user notifications |
| 20 | provider_earnings | Stores provider earning records |

### Database Relationships

- A user can have a customer, provider, or technician profile.
- A customer can have multiple addresses.
- A service category can contain multiple services.
- A provider can offer multiple services.
- A customer can create multiple bookings.
- A booking can have assignment records and related images.
- A booking can have associated payment and invoice records.
- Customers can submit reviews and complaints.
- Providers can have multiple technicians and availability slots.

Refer to the submitted ER diagram and database schema for the detailed relationships and foreign keys.

## 7. Project Folder Structure

The project is organized into separate frontend and backend applications.

```text
HomeServe/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── security.py
│   │   └── seed.py
│   │
│   ├── tests/
│   │   └── test_health.py
│   │
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   ├── .env.example
│   └── .gitignore
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── style.css
│   │
│   ├── index.html
│   ├── package.json
│   ├── .env.example
│   └── .gitignore
│
├── submission_documents/
│   ├── API_Documentation.md
│   ├── Test_Cases.xlsx
│   ├── Test_Cases.csv
│   ├── Test_Execution_Report.md
│   ├── Security_Checklist.md
│   └── HomeServe_Project_Report.docx
│
├── HomeServe_Final_Presentation.pptx
└── README.md
```

*Note: This is the starter submission package structure. Update the folder tree if additional modules, routes, or files are added during development.*

## 8. Software Requirements

Install the following software before running the application:

- Python 3.10 or later (use a version supported by the project dependencies).
- Node.js and npm.
- MySQL Server or XAMPP MySQL.
- SQLyog or another MySQL client.
- Visual Studio Code or PyCharm.
- Postman.
- Git.

## 9. Backend Installation and Setup

### Step 1: Open the Project

Open the project folder in VS Code or PyCharm.

Open the terminal and navigate to the backend folder:

```powershell
cd backend
```

### Step 2: Create a Virtual Environment

```powershell
py -m venv venv
```

### Step 3: Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

For development and testing dependencies:

```powershell
pip install -r requirements-dev.txt
```

### Step 5: Configure Environment Variables

Create a `.env` file by copying the example file:

```powershell
copy .env.example .env
```

Configure your database connection and secret key in `.env`.

Example:

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/homeserve_db

SECRET_KEY=REPLACE_WITH_A_LONG_RANDOM_SECRET
```

Use your actual MySQL username and password. Do not commit `.env` to GitHub.

### Step 6: Create the Database

Open SQLyog and execute:

```sql
CREATE DATABASE homeserve_db;
```

Ensure that the database name matches the configured connection string.

### Step 7: Initialize Database Tables

Run the database initialization command supported by the project:

```powershell
python -m app.seed
```

The application initializes its SQLAlchemy tables when configured to do so. Verify the actual database tables in SQLyog.

### Step 8: Start the Backend Server

```powershell
uvicorn app.main:app --reload
```

The backend will be available at:

`http://127.0.0.1:8000`

## 10. Frontend Installation and Setup

Open another terminal.

### Step 1: Navigate to Frontend

```powershell
cd frontend
```

### Step 2: Install Dependencies

```powershell
npm install
```

### Step 3: Configure Frontend Environment Variables

```powershell
copy .env.example .env
```

Set the backend API base URL according to the frontend configuration.

Example:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### Step 4: Start the Frontend

```powershell
npm run dev
```

The frontend development server will display its local URL in the terminal, normally:

`http://localhost:5173`

## 11. API Documentation

HomeServe provides REST APIs through the FastAPI backend.

### Swagger UI

Once the backend is running, open:

`http://127.0.0.1:8000/docs`

Swagger UI provides an interactive interface to:

- View available API endpoints.
- Understand request and response structures.
- Provide request parameters and JSON bodies.
- Execute API requests.
- Inspect response status codes.

### ReDoc

`http://127.0.0.1:8000/redoc`

### API Testing

Postman can be used to test API endpoints.

Test the following areas:

- User registration and login.
- Authentication and authorization.
- User profile management.
- Service categories and services.
- Address management.
- Booking creation and management.
- Payment-related endpoints.
- Reviews and complaints.

Refer to `submission_documents/API_Documentation.md` for the project API reference.

Only endpoints actually registered in the running backend should be considered implemented.

## 12. Authentication and Security

The project uses JWT-based authentication.

Security measures to implement and verify include:

- Secure password hashing.
- JWT token validation.
- Token expiration.
- Role-based access control.
- Input validation.
- Database query safety through SQLAlchemy.
- Environment-based secret management.
- CORS restrictions.
- HTTPS in production.
- Secure payment verification.
- File upload validation.
- Safe error handling.

Refer to `submission_documents/Security_Checklist.md` for the verification checklist.

## 13. Testing

Testing is required to verify the functionality, reliability, and security of the application.

### Testing Tools

| Tool | Purpose |
|---|---|
| Postman | API testing |
| Pytest | Backend testing |
| Playwright | Frontend end-to-end testing |
| Swagger UI | Interactive API testing |

### Main Testing Areas

1. User registration.
2. User login.
3. JWT authentication.
4. Role-based authorization.
5. Customer profile management.
6. Address management.
7. Service category management.
8. Service management.
9. Booking creation.
10. Booking assignment.
11. Payment handling.
12. Review submission.
13. Complaint management.
14. API error handling.
15. Application health checks.

### Execute Backend Tests

From the backend directory:

```powershell
pytest -v
```

For an HTML report, if `pytest-html` is installed:

```powershell
pytest --html=report.html --self-contained-html
```

Test cases are provided in:

- `submission_documents/Test_Cases.xlsx`
- `submission_documents/Test_Cases.csv`

Record actual execution results in:

`submission_documents/Test_Execution_Report.md`

Do not report tests as passed until they have actually been executed.

## 14. Git and GitHub Setup

Git is used for version control and GitHub is used to host the source code.

### Step 1: Initialize Git

From the main project directory:

```powershell
git init
```

### Step 2: Add Project Files

```powershell
git add .
```

### Step 3: Commit Changes

```powershell
git commit -m "Initial HomeServe project submission"
```

### Step 4: Create a GitHub Repository

Create a new repository named:

`HomeServe-Home-Services-Booking-SaaS`

### Step 5: Connect the Repository

Replace the URL with your actual GitHub repository URL:

```powershell
git branch -M main

git remote add origin YOUR_GITHUB_REPOSITORY_URL

git push -u origin main
```

Never upload `.env`, passwords, API keys, database credentials, or other secrets.

## 15. Deployment

The application can be deployed using the following services:

### Frontend Deployment
Platform: Vercel

General deployment steps:

1. Push the frontend source code to GitHub.
2. Import the repository into Vercel.
3. Configure the frontend root directory.
4. Add the production backend API URL as an environment variable.
5. Build and deploy the frontend.

### Backend Deployment
Platform: Render

General deployment steps:

1. Push the backend source code to GitHub.
2. Create a new web service on Render.
3. Configure the backend root directory.
4. Configure the Python build and start commands.
5. Add database connection and secret environment variables.
6. Configure production database connectivity.
7. Deploy and verify the API.

### Database Deployment

Use a production MySQL database accessible to the backend service.

### Deployment Verification

After deployment, verify:

- Frontend loads successfully.
- Backend health endpoint responds.
- Frontend can communicate with the backend.
- Authentication works.
- Database connectivity works.
- CORS is configured correctly.
- Secrets are configured securely.

Add the actual deployment URLs and screenshots to the final submission after successful deployment.

## 16. Payment and Image Integration

### Razorpay

Razorpay can be integrated for online service payments.

Expected integration activities:

- Create an order from the backend.
- Use the Razorpay checkout flow.
- Verify payment signatures on the backend.
- Validate payment webhooks.
- Store transaction references and payment statuses.

Use test mode until payment integration is fully tested.

### Cloudinary

Cloudinary can be used to store:

- Customer profile images.
- Provider documents.
- Service images.
- Booking-related images.

Validate file types, file sizes, and permissions before uploading.

These integrations must be configured and tested before being presented as completed features.

## 17. Expected Project Deliverables

The final HomeServe submission should contain:

1. Complete source code.
2. GitHub repository URL.
3. Live deployed application or deployment evidence.
4. Database schema.
5. Entity Relationship Diagram (ERD).
6. API documentation.
7. Test cases.
8. Test execution report.
9. Security checklist.
10. Project documentation.
11. AI prompts and development log.
12. Final project presentation.

## 18. Future Enhancements

- Real-time booking status updates.
- Live technician tracking.
- SMS and email notifications.
- Advanced admin analytics dashboard.
- AI-based service recommendations.
- AI chatbot for customer support.
- Automated provider recommendations.
- Advanced payment and refund management.
- Mobile application.
- Advanced reporting and business analytics.

## 19. AI-Assisted Development

AI tools may be used during development for:

- Understanding requirements.
- Generating code suggestions.
- Debugging errors.
- Designing database structures.
- Preparing API documentation.
- Generating test scenarios.
- Improving application security.
- Preparing project documentation.

All AI-generated code must be reviewed, tested, and validated before submission.

Maintain an AI development log containing:

- Date.
- AI tool used.
- Prompt.
- Generated output or suggestion.
- Changes made.
- Testing and verification results.

## 20. Conclusion

HomeServe is designed to provide a centralized solution for managing home service bookings and service provider operations.

The platform brings customers, service providers, technicians, and administrators together through a structured web application.

By combining React.js, FastAPI, Python, MySQL, and modern authentication practices, HomeServe provides a foundation for a scalable home services booking platform.

The project can be extended with payment processing, cloud image storage, real-time notifications, AI-powered recommendations, and production deployment.

---

**Project Name:** HomeServe – Home Services Booking SaaS Platform

**Project Type:** Full Stack Web Application

**Frontend:** React.js

**Backend:** Python FastAPI

**Database:** MySQL

**ORM:** SQLAlchemy

**API Architecture:** RESTful APIs

**Authentication:** JWT

**Version Control:** Git and GitHub
