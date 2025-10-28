from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication_date=models.DateField()
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name

class Reviews(models.Model):
    reviews=models.TextField()
    date_reviews=models.DateTimeField(auto_now_add=True)
    book=models.ForeignKey('Book',on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.reviews

