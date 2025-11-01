from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication_date=models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def color(self):
        colors = {
            "Fiction": "#ff6f61",
            "Non-Fiction": "#6fbfff",
            "Mystery": "#a34fff",
            "Science Fiction": "#ffa500",
            "Fantasy": "#4caf50",
            "Biography": "#ffde59"
        }
        return colors.get(self.category.name, "#cccccc")

    def icon(self):
        icons = {
            "Fiction": "bi-book-half",
            "Non-Fiction": "bi-journal-text",
            "Mystery": "bi-search",
            "Science Fiction": "bi-robot",
            "Fantasy": "bi-magic",
            "Biography": "bi-person-badge"
        }
        return icons.get(self.category.name, "bi-card-text")

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def color(self):
        colors = {
            "Fiction": "#ff6f61",
            "Non-Fiction": "#6fbfff",
            "Mystery": "#a34fff",
            "Science Fiction": "#ffa500",
            "Fantasy": "#4caf50",
            "Biography": "#ffde59"
        }
        return colors.get(self.name, "#cccccc")

    def icon(self):
        icons = {
            "Fiction": "bi-book-half",
            "Non-Fiction": "bi-journal-text",
            "Mystery": "bi-search",
            "Science Fiction": "bi-robot",
            "Fantasy": "bi-magic",
            "Biography": "bi-person-badge"
        }
        return icons.get(self.name, "bi-card-text")

    def total_reviews_count(self):
        return Reviews.objects.filter(book__category=self).count()

    def __str__(self):
        return self.name

class Reviews(models.Model):
    reviews=models.TextField()
    date_reviews=models.DateTimeField(auto_now_add=True)
    book=models.ForeignKey('Book',on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.reviews

