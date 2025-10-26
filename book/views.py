from django.shortcuts import render
from .models import Category,Book,Reviews
# Create your views here.

def index_views(request):
    last_reviews = Reviews.objects.order_by('-date_reviews')[:15]
    return render(request, 'book/index.html', {'last_reviews': last_reviews})


def categories_views(request):
    categories=Category.objects.all()
    return render(request, 'book/categories.html',
                  {'categories': categories})

def books_views(request):
    books=Book.objects.all().order_by('-publication_date')
    return render(request, 'book/books.html',
                  {'books': books})