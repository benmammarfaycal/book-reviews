from . import views
from django.urls import path

app_name= 'book'
urlpatterns = [
    path('', views.index_views,name='index'),
    path('/categories', views.categories_views,name='categories'),
    path('/books', views.books_views,name='books'),
    path('/add_review', views.book_reviews_form,name='add_review'),
]