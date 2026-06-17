# 📝 Django Todo CRUD App

A simple Todo List application built with Django to demonstrate basic CRUD (Create, Read, Update, Delete) operations.

---

## 🚀 Features

* Add new tasks
* View all tasks
* Update tasks
* Delete tasks
* Mark tasks as completed
* Admin panel support

---

## 🧰 Tech Stack

* Python 3.x
* Django
* SQLite (default database)

---

## 📁 Project Structure

```
todo_project/
├── manage.py
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│       └── todo/
│           ├── task_list.html
│           ├── add_task.html
│           └── update_task.html
```

---

## ⚙️ Installation & Setup

### 1. Clone repository

```
git clone https://github.com/robiulislam99/CRUD-to-do-list-using-Django.git
cd todo_project
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
```

### 3. Install dependencies

```
pip install django
```

### 4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (optional)

```
python manage.py createsuperuser
```

### 6. Run server

```
python manage.py runserver
```

Open browser:
👉 http://127.0.0.1:8000/

---

## 🔐 Admin Panel

Access admin panel:

 http://127.0.0.1:8000/admin/

---

## 📌 Learning Purpose

This project helps you understand:

* Django project structure
* Models & database
* Views and templates
* URL routing
* CRUD operations

---

## 🚀 Future Improvements

* Add authentication (login/register)
* Use Django Forms
* Add REST API (Django REST Framework)
* Improve UI with Bootstrap

---

## 👨‍💻 Author

Md Robiul Islam
