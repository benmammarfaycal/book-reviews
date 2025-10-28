from django import forms
from .models import Reviews

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
