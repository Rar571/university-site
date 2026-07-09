# 🎓 University Site

A web application built with **Django** for managing university data. The system provides an intuitive interface for administrators to manage students, teachers, and specializations through complete CRUD functionality.

## 🌐 Live Demo

**Application:** https://university-site-z5vi.onrender.com

---

## 📌 Overview

University Site is designed to simplify academic data management by providing a centralized platform for maintaining university records.

The application allows users to:

- Manage student records
- Manage teacher profiles
- Manage specializations
- Create, edit, view, and delete data
- Navigate through a clean and user-friendly interface

---

## ✨ Features

- ✅ Student management (CRUD)
- ✅ Teacher management (CRUD)
- ✅ Specialization management (CRUD)
- ✅ Django Forms for data validation
- ✅ SQLite database integration
- ✅ Responsive and clean UI
- ✅ Django Admin panel

---

## 🛠 Tech Stack

| Technology | Description |
|------------|-------------|
| **Python** | Programming language |
| **Django** | Backend framework |
| **HTML5** | Markup |
| **CSS3** | Styling |
| **SQLite** | Database |
| **Bootstrap** *(if used)* | UI components |

---

## 📂 Project Structure

```
university-site/
│
├── university_app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── university_site/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/Rar571/university-site.git
cd university-site
```

### 2. Create virtual environment

**Linux / macOS**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start development server

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## 🎯 Learning Objectives

This project demonstrates practical experience with:

- Django Models
- URL Routing
- Function-Based Views
- Django Forms
- CRUD Operations
- Database Design
- Template Inheritance
- Static Files
- MVC/MVT Architecture
- Deployment on Render
