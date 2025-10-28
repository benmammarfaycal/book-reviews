from django import forms
from .models import Reviews, Book

class AddReviewsForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields = ["book","reviews"]

        labels = {
            "book":"Book:",
            "reviews":"Your review"
        }

        widgets={
            "book": forms.Select(attrs={"class": "form-control", "placeholder": "Select a book"}),
            "reviews":forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Add a review", "rows": 5})

        }

class AddBooksForm(forms.ModelForm):
    class Meta:
        model=Book
        fields = ["title","author","publication_date","description","isbn","category"]

        labels={
            "title":"title:",
            "author":"author:",
            "publication_date":"publication_date:",
            "description":"description:",
            "isbn":"isbn:",
            "category":"category",
        }

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Book title"}),
            "author": forms.TextInput(attrs={"class": "form-control", "placeholder": "Author name"}),
            "publication_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Book description", "rows": 2}),
            "isbn": forms.TextInput(attrs={"class": "form-control", "placeholder": "ISBN"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }