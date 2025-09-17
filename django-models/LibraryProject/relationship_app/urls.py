# LibraryProject/relationship_app/urls.py
from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import register, admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # auth routes (Django's built-in LoginView/LogoutView with explicit templates)
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register, name="register"),

    # role-based views
    path("admin-area/", admin_view, name="admin_view"),
    path("librarian-area/", librarian_view, name="librarian_view"),
    path("member-area/", member_view, name="member_view"),

    # permission-protected book CRUD
    path("book/add/", add_book, name="add_book"),
    path("book/<int:pk>/edit/", edit_book, name="edit_book"),
    path("book/<int:pk>/delete/", delete_book, name="delete_book"),
]
