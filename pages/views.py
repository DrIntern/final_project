from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class BookeReviewView(TemplateView):
    template_name = 'pages/book_reviews.html'


