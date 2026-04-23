from django.db import models
from django.urls import reverse
from common.utils.text import unique_slug

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    first_published = models.DateField()
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False)

    def get_absolute_url(self):
        return reverse('books:detail', args=[self.slug])
    
    #overriding default save method
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title