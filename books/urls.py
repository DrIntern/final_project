from django.urls import path
from .views import (
    BookCreateView, BookDetailView, BookListView,
    BookUpdateView,BookDeleteView,)

app_name = 'books'
urlpatterns = [
    path('book/<slug>/update/', BookUpdateView.as_view(), name='update'),
    path('book/create/', BookCreateView.as_view(), name= 'create'),
    path('book/<slug>/',BookDetailView.as_view(), name='detail'),
    path('book/<slug>/delete/',BookDeleteView.as_view(),name='delete' ),
    path('', BookListView.as_view(), name='list'),
    
]