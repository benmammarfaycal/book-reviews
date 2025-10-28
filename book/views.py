from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AddReviewsForm, AddBooksForm
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


