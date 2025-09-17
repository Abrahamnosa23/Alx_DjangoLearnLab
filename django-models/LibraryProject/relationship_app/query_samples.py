# LibraryProject/relationship_app/query_samples.py
from .models import Author, Book, Library

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        return []
    return Book.objects.filter(author=author)

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return []
    return library.books.all()

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return None
    return getattr(library, 'librarian', None)
