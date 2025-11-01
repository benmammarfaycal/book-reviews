# ProjectReviews

A Django-based web application that allows users to browse books by category, view reviews, and manage their own book collection with a complete authentication system.

## 🚀 Features Implemented

### Core Features
- **User Authentication System** (Login, Register, Logout)
- **User Profiles** with personal statistics and activity tracking
- Display of all categories with custom background colors and icons
- Display of all books belonging to each category, styled with category-specific colors and icons
- Latest reviews section showing the most recent posted reviews
- Add new books to the collection
- Write and submit book reviews
- Responsive UI using Bootstrap 5 with modern design
- Project structured with multiple Django apps (books, contact)

### Authentication & User Management
- **User Registration** with form validation and security
- **Secure Login** with error handling and password visibility toggle
- **Protected Routes** for authenticated-only actions (adding books/reviews)
- **Automatic Redirection** to intended pages after login
- **User Profiles** showing:
  - Personal statistics (reviews written, books added)
  - Reader level based on activity
  - Recent activity timeline
  - Favorite categories
  - All user's reviews and added books

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5 + Bootstrap Icons + Custom CSS
- **Database:** SQLite (development)
- **Authentication:** Django built-in authentication system
- **Security:** CSRF protection, password hashing
- **Version Control:** Git & GitHub

## 📁 Project Structure
````
projectreviews/
│
├── manage.py
├── README.md
├── populate_db.py
│
├── projectreviews/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── book/ # Main app: categories, books, reviews, authentication
│ ├── templates/book/
│ │ ├── index.html # Homepage with stats and latest reviews
│ │ ├── login.html # Login page with error handling
│ │ ├── register.html # User registration
│ │ ├── profile.html # User profile with activity
│ │ ├── books.html # All books listing
│ │ ├── categories.html # All categories
│ │ ├── book_infos.html # Individual book details
│ │ ├── category_infos.html # Individual category details
│ │ ├── add_book_form.html # Form to add new books
│ │ └── add_review_form.html # Form to add reviews
│ ├── models.py # Book, Category, Reviews models
│ ├── views.py # All views including authentication
│ ├── urls.py # URL routing
│ ├── forms.py # Django forms for books and reviews
│ └── apps.py
│
└── contact/ # Contact form app
├── templates/contact/
└── ...
````


## 🔧 Installation (Local)

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd projectreviews
   
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run migrations:**
   ```bash
   python manage.py migrate
   
5. **Start the development server:**
   ```bash
   python manage.py runserver
   
6. **Visit the application:**
- 👉 http://127.0.0.1:8000/

## 👤 User Authentication
**Registration**
- Access via "Login" → "Create Account" or direct /register/ URL
- Secure password validation
- Automatic login after registration
- Redirects to intended page if interrupted during authentication

**Login Features**
- Modern login interface with gradient design
- Real-time form validation
- Password visibility toggle
- Error handling for invalid credentials
- Automatic redirection to previously attempted pages

**Protected Features (Require Login)**
- Add New Books (/add_book/)
- Write Reviews (/add_review/)
- View Profile (/profile/)

**Profile System**
- Personal Dashboard: View your reading statistics
- Activity Tracking: Timeline of your reviews and book additions
- Reader Levels: Beginner → Intermediate → Advanced → Expert
- Favorite Categories: Auto-detected based on your reviews
- Quick Actions: Easy access to common tasks

## 🏗️ Populate the Database:
- A Python script is provided to fill the database with initial data: categories, books, and reviews.
1. **Make sure your virtual environment is activated:**
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   
2. **Install dependencies if not already done:**
   ```bash
   pip install -r requirements.txt
3. **Run the populate script:**
   ```bash
   python populate_db.py

### 🔐 Authentication Flow:
1. **New Users:**
- Register account → Automatic login → Redirect to homepage
- Access protected features immediately
2. **Existing Users:**
- Login with credentials → Redirect to intended page
- Access all protected features
3. **Access Control:**
- Unauthenticated users see prompts to login when trying protected actions
- Automatic redirect to login with helpful messages
- Session management for seamless browsing
 
### ✅ Future Improvements
- Book search and filtering
- Review editing and deletion
- Book ratings system
- Social features (follow users, like reviews)
- Reading lists and bookmarks
- Email notifications
- Admin dashboard improvements
- API development
- Mobile app version



- ✍️ Author: Benmammar Faycal
- 📌 Status: Under active development
- 🐛 Issues: Please report via GitHub issues
- 💡 Contributions: Welcome via pull requests