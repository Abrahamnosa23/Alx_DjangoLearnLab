from django.urls import path
from .views imporrt list_books , LibraryDetailView
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryListView.as_view(), name="library_detail"),
]
