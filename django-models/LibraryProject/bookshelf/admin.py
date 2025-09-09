from django.contrib import admin

# Register your models here.

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('publication_year',)   # enables filtering in admin
    search_fields = ('title', 'author')   # enables search in admin
