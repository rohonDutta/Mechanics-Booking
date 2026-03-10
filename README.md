> **Visit **
https://mechanics-booking.vercel.app/

# Vehicle Service Management System

A web-based Django application designed to help manage and track vehicle service requests, mechanics, customers, and administrative tasks. 

## Features
- **Admin Panel**: Manage Mechanics, Customers, Service Requests, Attendance, Salary and generated Reports.
- **Customer Panel**: Create and view service requests, view service invoices, and manage profile.
- **Mechanic Panel**: Track assigned work, update work status, and view attendance/salary.

## Prerequisites

Before running the project locally, ensure you have the following installed on your system:
- **Python** (version 3.6 or higher)
- **pip** (Python package installer)

## Local Setup Instructions

Follow these steps to run the project on your local machine:

### 1. Clone or Download the Repository
Navigate to the directory where you'd like to run the project.

### 2. Create a Virtual Environment (Recommended)
Open your terminal or command prompt in the project root directory and run:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
Install all required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
Set up the SQLite database and create the necessary tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)
To access the Django Admin panel, you must create a superuser account:

```bash
python manage.py createsuperuser
```
*(Follow the prompt to provide a Username, Email (optional), and Password).*

### 6. Run the Development Server
Start the local server:

```bash
python manage.py runserver
```

The application will now be running at `http://127.0.0.1:8000/`.

## Accessing the Panels:
- **Main Website**: `http://127.0.0.1:8000/`
- **Django Admin Interface**: `http://127.0.0.1:8000/admin/`

## Troubleshooting

- **`ModuleNotFoundError` or `NameError` in settings / urls**: Ensure your virtual environment is activated and all dependencies in `requirements.txt` are correctly installed.
- **`DisallowedHost` Error**: Ensure that `ALLOWED_HOSTS` in `vehicleservicemanagement/settings.py` includes `localhost`, `127.0.0.1`, or `*`.

## Built With
- **Backend Framework**: Django (Python)
- **Database**: SQLite (Default Django DB)
- **Frontend**: HTML / CSS / JavaScript (Templates within Django)
