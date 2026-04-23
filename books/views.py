from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy

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

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')