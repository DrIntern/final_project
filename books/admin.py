from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'author', 'first_published']

    #might need this later
    #def get_readonly_fields(self, request, obj=None):
    #    if obj: # editing an existing object
    #        return ('created', 'updated')

    #    return ()