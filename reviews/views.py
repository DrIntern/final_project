from django.views.generic import ListView
from .models import Book

# Create your views here.

class BookListView(ListView):
    model = Book