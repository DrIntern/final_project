from django.forms import ModelForm, Textarea, DateInput

from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'first_published']
        widgets = {
            'title': Textarea(
                attrs={'cols': 80, 'rows': 1, 'autofocus': True, 'placeholder': 'Fiction only, please.'}
            ),
            'answer': Textarea(
                attrs={'cols': 80, 'rows': 1}
            ),
            'genre': Textarea(
                attrs={'cols': 80, 'rows': 1}
            ),
            'first_published': DateInput(
                attrs={'type': 'date'}
            )
        }
