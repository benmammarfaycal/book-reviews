# populate_data.py
import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectreviews.settings")
django.setup()

from book.models import Category, Book, Reviews
from django.contrib.auth.models import User

# --- 1. Créer les catégories ---
categories_data = [
    ("Fiction", "Imaginative storytelling and novels."),
    ("Non-Fiction", "Informative and factual books."),
    ("Mystery", "Books full of suspense and twists."),
    ("Science Fiction", "Futuristic and science-based stories."),
    ("Fantasy", "Magical worlds and adventures."),
    ("Biography", "Life stories of famous people."),
]

categories = {}
for name, description in categories_data:
    cat, created = Category.objects.get_or_create(name=name, defaults={"description": description})
    categories[name] = cat

# --- 2. Créer les livres ---
books_data = {
    "Fiction": [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_year": "1960-07-11", "description": "A novel about racial injustice in the Deep South.", "isbn": "9780061120084"},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "publication_year": "1813-01-28", "description": "A classic romance novel.", "isbn": "9780141439518"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publication_year": "1925-04-10", "description": "A story of wealth, love, and the American Dream.", "isbn": "9780743273565"},
    ],
    "Non-Fiction": [
        {"title": "Sapiens", "author": "Yuval Noah Harari", "publication_year": "2011-01-01", "description": "A brief history of humankind.", "isbn": "9780062316097"},
        {"title": "Educated", "author": "Tara Westover", "publication_year": "2018-02-20", "description": "A memoir about growing up in a strict household.", "isbn": "9780399590504"},
        {"title": "The Immortal Life of Henrietta Lacks", "author": "Rebecca Skloot", "publication_year": "2010-02-02", "description": "Story of the woman behind HeLa cells.", "isbn": "9781400052189"},
    ],
    "Mystery": [
        {"title": "Gone Girl", "author": "Gillian Flynn", "publication_year": "2012-06-05", "description": "A thriller about a missing wife.", "isbn": "9780307588371"},
        {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "publication_year": "2005-08-01", "description": "A mystery novel from Sweden.", "isbn": "9780307454546"},
        {"title": "Big Little Lies", "author": "Liane Moriarty", "publication_year": "2014-07-29", "description": "A story full of secrets and lies.", "isbn": "9780425274866"},
    ],
    "Science Fiction": [
        {"title": "Dune", "author": "Frank Herbert", "publication_year": "1965-08-01", "description": "Epic science fiction novel.", "isbn": "9780441172719"},
        {"title": "Ender's Game", "author": "Orson Scott Card", "publication_year": "1985-01-15", "description": "A story about a child genius in a war against aliens.", "isbn": "9780812550702"},
        {"title": "Neuromancer", "author": "William Gibson", "publication_year": "1984-07-01", "description": "Cyberpunk classic.", "isbn": "9780441569595"},
    ],
    "Fantasy": [
        {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "publication_year": "1997-06-26", "description": "The first book in the Harry Potter series.", "isbn": "9780590353427"},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "publication_year": "1937-09-21", "description": "A fantasy adventure with Bilbo Baggins.", "isbn": "9780345339683"},
        {"title": "A Game of Thrones", "author": "George R.R. Martin", "publication_year": "1996-08-06", "description": "First book of the Song of Ice and Fire series.", "isbn": "9780553103540"},
    ],
    "Biography": [
        {"title": "Steve Jobs", "author": "Walter Isaacson", "publication_year": "2011-10-24", "description": "Biography of Steve Jobs.", "isbn": "9781451648539"},
        {"title": "Becoming", "author": "Michelle Obama", "publication_year": "2018-11-13", "description": "Memoir by the former First Lady.", "isbn": "9781524763138"},
        {"title": "Long Walk to Freedom", "author": "Nelson Mandela", "publication_year": "1994-01-01", "description": "Autobiography of Nelson Mandela.", "isbn": "9780316548182"},
    ],
}

books = []
for cat_name, books_list in books_data.items():
    category = categories[cat_name]
    for book_info in books_list:
        book = Book.objects.create(
            title=book_info["title"],
            author=book_info["author"],
            publication_year=book_info["publication_year"],
            description=book_info["description"],
            isbn=book_info["isbn"],
            category=category,
            added_by=None
        )
        books.append(book)

# --- 3. Créer les avis ---
sample_reviews = [
    "Absolutely loved it! Highly recommended.",
    "An interesting read but could be shorter.",
    "Didn't enjoy it as much as I thought.",
    "A masterpiece! Will read again.",
    "Informative and engaging.",
    "I struggled to finish it, not my type.",
    "Beautifully written with deep characters.",
]

for book in books:
    num_reviews = random.randint(0, 3)
    for _ in range(num_reviews):
        review_text = random.choice(sample_reviews)
        review_date = datetime.now() - timedelta(days=random.randint(0, 365))
        Reviews.objects.create(
            reviews=review_text,
            date_reviews=review_date,
            book=book,
            posted_by=None
        )

print("Database populated successfully!")
#to lanch the script type in the terminal:python populate_data.py
