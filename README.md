# ProjectReviews

A Django-based web application that allows users to browse books by category and view the latest posted reviews.  
Each book is visually styled according to its category using unique icons and colors.

## 🚀 Features Implemented

- Display of all categories with a custom background color and icon.
- Display of all books belonging to each category, styled with the same color and icon as the category.
- Latest reviews section (showing the most recent posted reviews).
- Responsive UI using Bootstrap 5.
- Project structured with multiple Django apps (books, contact).

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5 + Bootstrap Icons
- **Database:** SQLite (development)
- **Version Control:** Git & GitHub

## 📁 Project Structure (simplified)
````
projectreviews/
│
├── manage.py
├── README.md
│
├── book/ # Handles categories & books & reviews 
├── contact/ # Contact form pages
````
bash
Copier le code

## 🔧 Installation (Local)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd projectreviews
2. Create and activate a virtual environment:

   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run migrations:
    ```bash
    python manage.py migrate

5. Start the development server:
    ```bash
    python manage.py runserver
Visit:
👉 http://127.0.0.1:8000/

## 🏗️ Populate the Database

A Python script is provided to fill the database with initial data: categories, books, and reviews.

1. Make sure your virtual environment is activated and dependencies are installed:

   ```bash
   pip install -r requirements.txt
2. Run the populate script:
    ```bash
    python populate_db.py
   
## ✅ Future Improvements
- User authentication (login/register system)
- Add review submission via UI
- Pagination for long lists
- Search bar for books
- Admin dashboard improvements

✍️ Author: Benmammar Faycal
📌 Status: Under development