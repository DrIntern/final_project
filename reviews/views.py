from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import Book

# Create your views here.

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'first_published']

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'genre', 'first_published']