# Library Management System API

A simple Flask-based API for managing a library system. This application allows CRUD operations for books and members. It includes optional features like search functionality and pagination.

## Features
- Add, view, update, and delete books and members.
- Search for books by title or author.
- Pagination for listing books and members.
- Token-based authentication (optional).

## Requirements
- Python 3.7 or higher
- Flask 2.x or higher

## Setup Instructions

### 1. Clone the Repository
bash
git clone https://github.com/<your-username>/LibraryManagementSystem.git
cd LibraryManagementSystem


#Create a virtual environment 
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

#Install Dependencies 
pip install -r requirements.txt

#Run the applications
python app.py

