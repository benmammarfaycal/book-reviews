from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AddReviewsForm, AddBooksForm, CustomAuthenticationForm
from .models import Category,Book,Reviews
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
# Create your views here.

def index_views(request):
    last_reviews = Reviews.objects.order_by('-date_reviews')[:15]

    # Add stats
    total_books = Book.objects.count()
    total_categories = Category.objects.count()
    total_reviews = Reviews.objects.count()
    total_users = User.objects.count()
    user = request.user
    context = {
        'last_reviews': last_reviews,
        'total_books': total_books,
        'total_categories': total_categories,
        'total_reviews': total_reviews,
        'total_users': total_users,
        'user':user
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

@login_required
def book_reviews_form(request):
    if not request.user.is_authenticated:
        request.session['next_url'] = request.path
        messages.warning(request, "Only connected users can add reviews.")
        return redirect('book:login')

    if request.method == "POST":
        form = AddReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.posted_by = request.user
            review.save()
            messages.success(request, "You added a review successfully")
            return redirect('book:add_review')
    else:
        form = AddReviewsForm()

    return render(request, 'book/add_review_form.html',
                  {'form': form})

@login_required
def add_books_form(request):
    if not request.user.is_authenticated:
        request.session['next_url'] = request.path
        messages.warning(request, "Only connected users can add books.")
        return redirect('book:login')

    if request.method == "POST":
        form = AddBooksForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            messages.success(request, "You added a book successfully")
            return redirect('book:add_book')
    else:
        form = AddBooksForm()

    return render(request, 'book/add_book_form.html', {'form': form})


def category_infos(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'book/category_infos.html', {'category': category})

def book_infos(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_infos.html', {'book': book})


class CustomLoginView(LoginView):
    template_name = "book/login.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.session.pop('next_url', None)
        if next_url:
            return next_url
        return super().get_success_url()


class CustomLogoutView(LogoutView):
    next_page = "book:index"

    def dispatch(self, request, *args, **kwargs):
        current_path = request.path
        if not any(protected in current_path for protected in ['/add_book', '/add_review']):
            request.session['logout_redirect'] = current_path
        response = super().dispatch(request, *args, **kwargs)
        logout_redirect = request.session.pop('logout_redirect', None)
        if logout_redirect:
            return HttpResponseRedirect(logout_redirect)

        return response


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            next_url = request.session.pop('next_url', None)
            if next_url:
                return redirect(next_url)
            return redirect("book:index")
    else:
        form = UserCreationForm()
    return render(request, "book/register.html", {"form": form})


@login_required
def profile_view(request):
    user = request.user

    user_reviews = Reviews.objects.filter(posted_by=user).select_related('book', 'book__category').order_by(
        '-date_reviews')

    user_books = Book.objects.filter(added_by=user).select_related('category').order_by('-id')

    total_reviews = user_reviews.count()
    total_books_added = user_books.count()

    reader_level = "Beginner"
    if total_reviews > 20:
        reader_level = "Expert"
    elif total_reviews > 10:
        reader_level = "Advanced"
    elif total_reviews > 5:
        reader_level = "Intermediate"


    thirty_days_ago = timezone.now() - timedelta(days=30)
    recent_activity = []


    for review in user_reviews.filter(date_reviews__gte=thirty_days_ago):
        recent_activity.append({
            'type': 'review',
            'object': review,
            'date': review.date_reviews
        })


    for book in user_books.filter(added_by=user):
        recent_activity.append({
            'type': 'book',
            'object': book,
            'date': user.date_joined
        })

    recent_activity.sort(key=lambda x: x['date'], reverse=True)

    favorite_categories = Book.objects.filter(
        reviews__posted_by=user
    ).values(
        'category__name'
    ).annotate(
        count=Count('category')
    ).order_by('-count')[:3]

    context = {
        'user_profile': user,
        'user_reviews': user_reviews,
        'user_books': user_books,
        'total_reviews': total_reviews,
        'total_books_added': total_books_added,
        'reader_level': reader_level,
        'recent_activity': recent_activity[:10],
        'favorite_categories': favorite_categories,
    }

    return render(request, 'book/profile.html', context)