from django.urls import path
from .views import BookListView

app_name = 'reviews'
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
]