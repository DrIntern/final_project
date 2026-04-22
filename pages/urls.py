from django.urls import path

from .views import HomePageView, BookeReviewView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('book-reviews/', BookeReviewView.as_view(), name='book-reviews'),
]