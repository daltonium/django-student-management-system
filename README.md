# Django Student Management System

A full-stack web application built with Django 6 and PostgreSQL for managing students, teachers, courses, enrollments, and grades. Built as a learning project to understand relational database design, Django's ORM, class-based views, and admin customization.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0.3 |
| Database | PostgreSQL |
| DB Adapter | psycopg2-binary |
| Frontend | Django Templates + Custom CSS |
| Python | 3.14 |

---

## Features

- Student, Teacher, Course — full CRUD (Create, Read, Update, Delete)
- Enrollment tracking with duplicate prevention enforced at database level
- Grade management with filtered enrollment dropdown
- Per-student and per-course reports using SQL aggregation (AVG, COUNT, MAX, MIN)
- Django Admin with custom columns, search, filters, and inline grades
- Dashboard with live stat cards and recent activity
- Dark theme UI with custom color palette
- N+1 query prevention using `select_related` throughout
- Namespaced URLs, active navbar, template inheritance

---

## Color Palette

| Name | Hex |
|---|---|
| Obsidian | `#1E1E1E` |
| Steel Grey | `#636E72` |
| Racing Red | `#D63031` |
| Light Concrete | `#DFE6E9` |

---

## Project Structure

```
django-student-management-system/
├── core/                     # Project config
│   ├── settings.py
│   └── urls.py
├── students/                 # Main app
│   ├── models.py             # 5 database models
│   ├── views.py              # All class-based views
│   ├── forms.py              # ModelForms
│   ├── urls.py               # Namespaced URL patterns
│   ├── admin.py              # Customized admin
│   └── migrations/
├── templates/
│   ├── base.html             # Global layout
│   ├── dashboard.html        # Homepage
│   └── students/             # App templates (12 files)
├── static/
│   └── css/style.css         # Full dark theme
└── manage.py
```

---

## Database Schema

```
Teacher ──< Course
Student >──< Course  (via Enrollment junction table)
Enrollment ──  Grade (OneToOne)
```

| Model | Key Fields | Relationship |
|---|---|---|
| Student | first_name, last_name, email, date_of_birth | — |
| Teacher | first_name, last_name, email, department | — |
| Course | title, code | ForeignKey → Teacher |
| Enrollment | enrolled_on | ForeignKey → Student, Course |
| Grade | score, letter_grade, remarks | OneToOneField → Enrollment |

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/django-student-management-system.git
cd django-student-management-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django psycopg2-binary
```

### 4. Set up PostgreSQL

Open pgAdmin 4 or psql and run:

```sql
CREATE DATABASE student_mgmt;
CREATE USER student_admin WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE student_mgmt TO student_admin;
```

### 5. Configure the database

Open `core/settings.py` and update the `DATABASES` section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'student_mgmt',
        'USER': 'student_admin',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`

---

## URL Reference

| URL | Page |
|---|---|
| `/` | Dashboard |
| `/students/` | Student list |
| `/students/add/` | Add student |
| `/students/<pk>/edit/` | Edit student |
| `/students/<pk>/delete/` | Delete student |
| `/students/teachers/` | Teacher list |
| `/students/teachers/add/` | Add teacher |
| `/students/courses/` | Course list |
| `/students/courses/add/` | Add course |
| `/students/enrollments/` | Enrollment list |
| `/students/enrollments/add/` | Enroll student |
| `/students/grades/` | Grade list |
| `/students/grades/add/` | Add grade |
| `/students/reports/` | Reports page |
| `/admin/` | Django admin panel |

---

## Key Concepts Learned

- **Relational database design** — ForeignKey, OneToOneField, junction tables, unique_together constraints
- **Django ORM** — select_related, annotate, Avg, Count, Max, Min, values_list, queryset slicing
- **Class-based views** — ListView, CreateView, UpdateView, DeleteView, TemplateView
- **Django Admin customization** — list_display, search_fields, list_filter, inlines, custom columns
- **N+1 query prevention** — select_related resolves FK lookups in a single SQL JOIN
- **Template inheritance** — base.html with block content, {% extends %}, {% block %}
- **Static files** — STATICFILES_DIRS, STATIC_URL, {% load static %}, {% static %}
- **Form customization** — ModelForm __init__ override, queryset filtering, form_valid hook
- **URL namespacing** — app_name, reverse_lazy, {% url 'namespace:name' %}

---

## Django Commands Reference

```bash
python manage.py startproject name     # Create project
python manage.py startapp name         # Create app
python manage.py makemigrations        # Detect model changes
python manage.py migrate               # Apply to PostgreSQL
python manage.py createsuperuser       # Create admin user
python manage.py runserver             # Start dev server
python manage.py shell                 # Interactive Django shell
```

---

## License

This project is for learning purposes.
