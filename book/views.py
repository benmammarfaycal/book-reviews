from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AddReviewsForm, AddBooksForm
from .models import Category,Book,Reviews
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User



# Create your views here.

def index_views(request):
    last_reviews = Reviews.objects.order_by('-date_reviews')[:15]

    # Ajouter les statistiques
    total_books = Book.objects.count()
    total_categories = Category.objects.count()
    total_reviews = Reviews.objects.count()
    total_users = User.objects.count()

    context = {
        'last_reviews': last_reviews,
        'total_books': total_books,
        'total_categories': total_categories,
        'total_reviews': total_reviews,
        'total_users': total_users,
    }
    return render(request, 'book/index.html', context)


def categories_views(request):
    categories=Category.objects.all()
    return render(request, 'book/categories.html',
                  {'categories': categories})

def books_views(request):
    books=Book.objects.all().order_by('-publication_date')
    return render(request, 'book/books.html',
                  {'books': books})

def book_reviews_form(request):
    if request.method=="POST":
        form=AddReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You added a review successfully")
            return redirect('book:add_review')
    else:
        form=AddReviewsForm()

    return render(request, 'book/add_review_form.html',
                  {'form':form })


def add_books_form(request):
    if request.method=="POST":
        form=AddBooksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You added a book successfully")
            return redirect('book:add_book')
    else:
        form=AddBooksForm()

    return render(request,'book/add_book_form.html',{'form':form})


def category_infos(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'book/category_infos.html', {'category': category})

def book_infos(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_infos.html', {'book': book})