from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    books = models.ManyToManyField(Book, related_name='collections')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} by {self.user.username}"
