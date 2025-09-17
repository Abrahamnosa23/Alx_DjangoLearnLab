from django.shortcuts import render

# Create your views here.



from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book  # make sure Book model exists in bookshelf/models.py

@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # get all books from the DB
    return render(request, 'bookshelf/book_list.html', {'books': books})
