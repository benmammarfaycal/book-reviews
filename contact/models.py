from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_send = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        ordering = ['-date_send']

    def __str__(self):
        return f"{self.name}: {self.subject}"