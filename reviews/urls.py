from django.urls import path
from .views import (
    BookCreateView, BookDetailView, BookListView,
    BookUpdateView,)

app_name = 'reviews'
urlpatterns = [
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='update'),
    path('book/create/', BookCreateView.as_view(), name= 'create'),
    path('book/<int:pk>/',BookDetailView.as_view(), name='detail'),
    path('', BookListView.as_view(), name='list'),
    
]