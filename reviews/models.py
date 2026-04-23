from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.TextField(max_length=100)
    author = models.TextField(max_length=100)
    genre = models.TextField(max_length=100,)
    publication = models.DateField()

    def get_absolute_url(self):
        return reverse('reviews:detail', args=[str(self.pk)])

    def __str__(self):
        return self.title