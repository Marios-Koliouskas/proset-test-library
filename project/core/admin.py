from django.contrib import admin

# Register your models here. 

# Bring models from models.py
from .models import Author, Category, Book

# Show models in admin panel
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)