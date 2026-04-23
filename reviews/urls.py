from django.urls import path
from .views import BookDetailView, BookListView

app_name = 'reviews'
urlpatterns = [
    path('book/<int:pk>/',BookDetailView.as_view(), name='detail'),
    path('', BookListView.as_view(), name='list'),
    
]