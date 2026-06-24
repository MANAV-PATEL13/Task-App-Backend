# ⚡FastAPI Task Management System

A professional, asynchronous, and robust Task Management REST API built with **FastAPI**, **SQLAlchemy ORM**, **PostgreSQL**, and secured using **JWT (JSON Web Token)** authentication. This project features user authorization and complete CRUD capability for user-specific task flows, backed by database migrations with **Alembic**.

---

## 🚀 Features

* **🔐 User Authentication**: 
  * Registration & Login with secure password hashing via `pwdlib`.
  * JWT token generation with configurable expiration time.
  * Active authentication check endpoint (`/user/is_auth`).
* **📋 Task Management (CRUD)**:
  * Users can create, read, update, and delete their tasks.
  * Strict ownership validation: users can only view or manage their own tasks.
  * Task status tracking (Completed / Pending).
* **⚙️ Configuration Management**:
  * Seamless environment variables loading using `pydantic-settings` from a `.env` file.
* **🗄️ Database Migrations**:
  * Full support for database versioning and migrations using Alembic.
* **📄 Interactive Documentation**:
  * Auto-generated Swagger UI (`/docs`) and ReDoc (`/redoc`) API documentation.

---

## 🛠️ Tech Stack & Dependencies

* **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous, high performance)
* **ASGI Web Server**: [Uvicorn](https://www.uvicorn.org/)
* **ORM**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/)
* **Database**: PostgreSQL (via `psycopg2-binary` driver)
* **Validation**: [Pydantic v2](https://docs.pydantic.dev/)
* **Security**: `pwdlib` (modern password hashing) & `PyJWT` (JSON Web Tokens)
* **Migrations**: [Alembic](https://alembic.oturberey.net/)

---

## 📂 Project Structure

The project structure is organized cleanly separating concerns across modules:

```
Task Management/
├── src/
│   ├── tasks/             # Tasks Module
│   │   ├── controller.py  # Task business logic (create, get, update, delete)
│   │   ├── dtos.py        # Pydantic schemas for request/response validation
│   │   ├── models.py      # SQLAlchemy database model for Tasks (user_tasks table)
│   │   └── router.py      # FastAPI router defining task endpoints
│   ├── user/              # User Authentication Module
│   │   ├── controller.py  # User registration, verification, login, JWT helpers
│   │   ├── dtos.py        # Pydantic schemas for user registration, response, login
│   │   ├── models.py      # SQLAlchemy database model for Users (user_table table)
│   │   └── router.py      # FastAPI router defining authentication endpoints
│   └── utils/             # Core Utilities
│       ├── constent.py    # Global constants
│       ├── db.py          # SQLAlchemy base, engine, and get_db session dependency
│       ├── helpers.py     # Authentication dependency (is_authenticated checking JWT)
│       └── settings.py    # Pydantic Settings class to manage configurations
├── migrations/            # Alembic migrations history and scripts
│   └── versions/          # Individual database migration files
├── alembic.ini            # Alembic configuration file
├── main.py                # Main application entry point (FastAPI app setup)
├── requirement.txt        # Python dependency requirements
├── .env                   # Local configuration environment variables (git-ignored)
└── .env.example           # Reference guide template for environment configuration
```

---

## ⚙️ Setup & Installation

### 1. Clone & Navigate to Project
```bash
cd "Task Management"
```

### 2. Set Up Virtual Environment
Create and activate a virtual environment to isolate project dependencies:

* **Windows (PowerShell)**:
  ```powershell
  python -m venv env
  .\env\Scripts\Activate.ps1
  ```
* **macOS / Linux**:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and adjust the variables with your local database information:
```bash
cp .env.example .env
```
Ensure your configuration contains valid credentials:
```env
DB_CONNECTION="postgresql://<db_username>:<db_password>@localhost:5432/<db_name>"
SECRET_KEY="your-random-generated-jwt-secret-key"
ALGORITHM="HS256"
EXP_TIME=30
```

### 5. Run Database Migrations
Initialize database schema via Alembic migrations:
```bash
alembic upgrade head
```

---

## 📡 API Endpoints

### 🔐 User & Auth Endpoints
| HTTP Method | Endpoint | Auth Required | Description |
| :--- | :--- | :---: | :--- |
| `POST` | `/user/register` | ❌ No | Registers a new user account with hashed password. |
| `POST` | `/user/login` | ❌ No | Authenticates user credentials & returns a JWT access token. |
| `GET` | `/user/is_auth` |  Yes | Validates JWT token and returns the current user profile. |

### 📋 Task Endpoints
| HTTP Method | Endpoint | Auth Required | Description |
| :--- | :--- | :---: | :--- |
| `POST` | `/tasks/create` |  Yes | Creates a new task under the current user's profile. |
| `GET` | `/tasks/all_task` |  Yes | Retrieves all tasks belonging to the current user. |
| `GET` | `/tasks/task/{id}` |  Yes | Retrieves details of a specific task. |
| `PUT` | `/tasks/update/{id}` |  Yes | Updates a task's title, description, or completion status. |
| `DELETE` | `/tasks/delete/{id}` |  Yes | Deletes a specific task. |

> **Authorization Protocol**: Add the header `Authorization: Bearer <your_jwt_token>` for all authenticated (` Yes`) endpoints.

---

## 🏃 Running the Application

Launch the local development server with auto-reload:
```bash
uvicorn main:APP --reload
```

The application runs on **[http://127.0.0.1:8000](http://127.0.0.1:8000)** by default.

* **Swagger UI Documentation**: Check [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test endpoints directly inside your browser.
* **Redoc Documentation**: Check [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) for clean, readable API schemas.

---

## 👤 Author

* **Developer**: Manav Patel
* **GitHub**: [MANAV-PATEL13](https://github.com/MANAV-PATEL13)
* **Email**: [manavjpatel2006@gmail.com](mailto:manavjpatel2006@gmail.com)

