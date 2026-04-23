from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    first_published = models.DateField()

    def get_absolute_url(self):
        return reverse('books:detail', args=[str(self.pk)])

    def __str__(self):
        return self.title