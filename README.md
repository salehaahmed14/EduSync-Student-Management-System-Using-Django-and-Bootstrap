# Student-Management-System-Using-Django-and-Bootstrap
This project is a basic django based web application. It uses django for its backend and HTML, CSS and Bootstrap to create the frontend and sqlite as its database. Via this simple Student Management System one can perform CRUD (Create, Read, Update and Delete) Operations on the student records. 
# Django Project - Getting Started Guide

This guide provides instructions for setting up and running a Django project on a Windows machine.
## Prerequisites
1. **Python**: Make sure you have Python 3.6 or newer installed. You can download Python from the official website: https://www.python.org/downloads/
## Setup Instructions
1. **Clone the Repository**
2. **Create a Virtual Environment (Optional but Recommended)**:
python -m venv venv   
venv\Scripts\activate
3. **Install Django**:
pip install django
4. **Create a Superuser** (for accessing Django Admin):
python manage.py createsuperuser
5. **Run the Development Server**:
python manage.py runserver
Navigate to: http://127.0.0.1:8000/
Django's development server runs by default on 127.0.0.1 (which is the local IP address) and uses port 8000. When you run the command python manage.py runserver, the development server starts, and you can access your project by opening your web browser and entering the above URL.
