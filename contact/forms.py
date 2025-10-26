from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["name","email","subject","message"]

        labels={
            "name":"Your name:",
            "email":"Your email:",
            "subject":"The subject:",
            "message":"Your message:",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez votre nom"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Entrez votre email"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez le sujet"}),
            "message": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Écrivez votre message", "rows": 5}),
        }