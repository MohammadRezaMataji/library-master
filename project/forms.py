from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'book_image' , 'demo_link', 'source_link', 'tags' ]