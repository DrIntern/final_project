from django.views.generic import DetailView, ListView
from .models import Book

# Create your views here.

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book