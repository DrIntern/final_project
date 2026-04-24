from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy
from .forms import BookForm

# Create your views here.

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')