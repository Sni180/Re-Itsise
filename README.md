# Re Itsise - Community Fault Reporting Platform

**See, Inform, Track — Together**

A Django-based web application that empowers communities to report, track, and manage infrastructure issues (faults) in real-time. Re Itsise is designed to facilitate communication between residents and service providers about infrastructure problems like water leaks, burst pipes, potholes, and electrical issues.

---

## Table of Contents

- [Features](#features)
- [Project Overview](#project-overview)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Database Models](#database-models)
- [URLs & Endpoints](#urls--endpoints)
- [Features in Detail](#features-in-detail)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Core Features

- **📍 Fault Reporting**: Users can log infrastructure issues with location, category, description, images, and audio evidence
- **🔍 Search & Discovery**: Search reports by location, category name, or reference number
- **👥 Community Participation**: Mark yourself as affected by a reported issue to stay updated
- **📊 Real-time Status Tracking**: Track fault status from Logged → Dispatched → In Progress → Resolved
- **📱 Responsive Design**: Mobile-friendly interface with modern UI/UX
- **🏷️ Categorized Issues**: Support for multiple fault categories including:
  - ⚡ Electricity Issues
  - 💧 Water Leaks
  - 🌊 Burst Pipes
  - 🕳️ Missing Manholes
  - 🏗️ Rubble
  - ⛈️ Storm Water
  - 🚽 Sanitation
  - 🚧 Potholes
  - 🌳 Other Issues

### Additional Features

- Admin dashboard for managing reports
- Multi-step report creation process
- Evidence collection (photos and audio)
- Automatic reference number generation
- Community activity timeline

---

## Project Overview

### Purpose

Re Itsise creates a bridge between communities and service providers by:
- Enabling transparent, real-time reporting of infrastructure issues
- Allowing multiple residents to join and track the same issue
- Maintaining accountability through status tracking
- Building community awareness of ongoing work

### Target Users

- **Residents**: Report issues and stay informed about repairs
- **Service Providers**: Manage and track incoming reports
- **Administrators**: Monitor platform activity and manage content

---

## Technology Stack

- **Backend**: Django 6.0.3
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: Pillow (PIL)
- **Database Tools**: sqlparse
- **Additional Libraries**:
  - asgiref (3.11.1) - Async utilities
  - tzdata (2025.3) - Timezone information

---

## Project Structure

```
ReitsiseSolution/
├── env/                           # Python virtual environment
├── reitsise/                       # Main Django project directory
│   ├── manage.py                   # Django management script
│   ├── db.sqlite3                  # SQLite database
│   ├── reitsise/                   # Main project settings
│   │   ├── __init__.py
│   │   ├── asgi.py                 # ASGI configuration
│   │   ├── wsgi.py                 # WSGI configuration
│   │   ├── settings.py             # Django settings
│   │   └── urls.py                 # Project URL routing
│   ├── map/                        # Map/Explorer app
│   │   ├── models.py               # Fault and AffectedResident models
│   │   ├── views.py                # View logic for map explorer
│   │   ├── urls.py                 # App URL patterns
│   │   ├── admin.py                # Admin configuration
│   │   ├── forms.py                # Form definitions
│   │   ├── migrations/             # Database migrations
│   │   └── templates/
│   │       └── map/
│   │           ├── index.html      # Main fault explorer page
│   │           ├── about.html      # About page
│   │           └── help.html       # Help/FAQ page
│   ├── fault_reporter/             # Fault reporting app
│   │   ├── models.py
│   │   ├── views.py                # Report creation logic
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── forms.py                # Report forms
│   │   ├── migrations/
│   │   └── templates/
│   │       └── fault_reporter/
│   ├── static/                     # Static assets (CSS, JS, images)
│   │   └── images/
│   ├── media/                      # User-uploaded files
│   │   └── fault_images/
│   └── templates/
│       └── base.html               # Base template
└── README.md                        # This file
```

---

## Installation & Setup

### Prerequisites

- Python 3.8+ 
- pip (Python package manager)
- Virtual environment tool (venv)

### Step 1: Clone/Setup the Project

```bash
cd ReitsiseSolution
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install django==6.0.3
pip install pillow
pip install sqlparse
```

Or install all at once using requirements (if available):

```bash
pip install -r requirements.txt
```

### Step 4: Setup Database

```bash
cd reitsise
python manage.py migrate
```

### Step 5: Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

---

## Running the Application

### Start Development Server

```bash
cd reitsise
python manage.py runserver
```

The application will be available at:
- **Main Application**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Access the Application

1. **Explore Reports**: Visit the home page to see community reports
2. **Report New Fault**: Click "LOG REPORT" button to create a new report
3. **Mark as Affected**: Click "I'm Affected" on any report to join it
4. **Search**: Use the search bar to find reports by location, category, or reference number

---

## Database Models

### Fault Model

Represents an infrastructure issue report.

**Fields:**
- `ref_number` (CharField): Unique reference number (auto-generated as RI-XXXXXX)
- `full_name` (CharField): Reporter's full name
- `cellphone` (CharField): Reporter's phone number
- `category` (CharField): Type of fault (ELEC, WLEAK, BPIPE, etc.)
- `location_address` (TextField): Description of fault location
- `latitude` (DecimalField): GPS latitude
- `longitude` (DecimalField): GPS longitude
- `description` (TextField): Detailed problem description
- `image` (ImageField): Photo evidence of the fault
- `audio_report` (FileField): Audio recording of the report
- `status` (CharField): Current status (LOG, DIS, PROG, RES)
- `date_reported` (DateTimeField): Timestamp of report creation

**Methods:**
- `save()`: Auto-generates reference number if not provided
- `icon` property: Returns emoji icon for the fault category

### AffectedResident Model

Represents residents who are affected by a reported fault.

**Fields:**
- `fault` (ForeignKey): Reference to the Fault being affected by
- `full_name` (CharField): Resident's name
- `cellphone` (CharField): Resident's phone number
- `date_joined` (DateTimeField): When they marked themselves as affected

---

## URLs & Endpoints

### Map/Explorer App

| URL | View | Name | Description |
|-----|------|------|-------------|
| `/` | `explorer_map` | `explorer_map` | Main fault explorer - displays all reports with search |
| `/about/` | `about` | `about` | About page |
| `/help/` | `help_faq` | `help` | Help and FAQ page |

### Fault Reporter App

| URL | View | Description |
|-----|------|-------------|
| `/report/` | `report` | Report creation form |
| `/im-affected/` | `im_affected` | Mark yourself as affected by a fault |

---

## Features in Detail

### 1. Fault Explorer (Homepage)

- **Search Functionality**: Search reports by:
  - Location address
  - Fault category (with keyword mapping)
  - Reference number
  - Description text
  
- **Report Cards**: Each report displays:
  - Category with emoji icon
  - Location and description
  - Current status with progress bar
  - Time since reported (relative time)
  - Number of affected residents
  - "I'm Affected" button

- **Live Status**: Shows "Kimberley Live" indicating the active location

### 2. Report Creation

Multi-step process to collect:
- **Step 1**: Reporter's name and phone number
- **Step 2**: Fault category and location details
- **Step 3**: Description, photo evidence, and optional audio

### 3. "I'm Affected" Feature

- Modal dialog for residents to join an existing report
- Collects affected resident's name and phone number
- Updates affected resident count
- Notifications sent to joined residents on status updates

### 4. Status Tracking

Four-stage workflow with visual progress indicator:
1. **LOG** (25%): Issue logged in system
2. **DIS** (50%): Dispatched to service team
3. **PROG** (75%): Currently being worked on
4. **RES** (100%): Problem resolved

---

## Configuration

### Django Settings (`reitsise/settings.py`)

**Current Configuration:**
- `DEBUG = True` (Development mode - change to False for production)
- `ALLOWED_HOSTS = []` (Add production domains here)
- `INSTALLED_APPS`: Includes 'map' and 'fault_reporter'
- Database: SQLite3 (db.sqlite3)

**Important Security Settings for Production:**

```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = 'your-production-secret-key'  # Do NOT use default
```

### Database Configuration

The project uses SQLite3. To use PostgreSQL or MySQL in production:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'reitsise_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Common Commands

### Database Operations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations
```

### User Management

```bash
# Create admin user
python manage.py createsuperuser

# Change password
python manage.py changepassword username
```

### Development

```bash
# Run development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Shell (interactive Python with Django context)
python manage.py shell
```

### Static Files

```bash
# Collect static files (production)
python manage.py collectstatic
```

---

## Troubleshooting

### Virtual Environment Issues

```bash
# If activation fails on Windows:
env\Scripts\activate.bat

# If pip install fails, upgrade pip first:
python -m pip install --upgrade pip
```

### Database Issues

```bash
# Reset database (WARNING: Loses all data)
python manage.py migrate zero [app_name]
python manage.py migrate

# Check migrations status
python manage.py showmigrations
```

### Port Already in Use

```bash
# Run on different port
python manage.py runserver 8080
```

---

## API Integration Notes

The "I'm Affected" feature uses JavaScript fetch API to POST data:

```javascript
fetch("{% url 'im_affected' %}", {
  method: "POST",
  body: new FormData(formElement),
  headers: { "X-CSRFToken": "{{ csrf_token }}" }
});
```

CSRF tokens are required for all POST requests.

---

## Future Enhancements

Potential features for future versions:
- Real-time map visualization with markers
- Email/SMS notifications
- File upload management
- Advanced filtering and reporting
- API for third-party integrations
- Mobile app
- Analytics dashboard
- Automated status updates

---

## Contributing

To contribute to this project:

1. Create a feature branch (`git checkout -b feature/YourFeature`)
2. Make your changes
3. Test thoroughly
4. Commit with clear messages
5. Push to the branch
6. Create a Pull Request

---

## Support

For issues, questions, or suggestions:
- Check the Help/FAQ page in the application
- Contact the development team
- Review Django documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)

---

## License

This project is part of Sol Plaatje University's Django Learning Projects.

---

## Project Information

- **Project Name**: Re Itsise
- **Version**: 1.0
- **Created**: 2026
- **Institution**: Sol Plaatje University
- **Django Version**: 6.0.3
- **Python Version**: 3.8+

---

**Re Itsise - Making Communities Safer and More Responsive** 🚀
