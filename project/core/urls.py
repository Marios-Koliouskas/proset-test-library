from django.urls import path
from . import views

urlpatterns = [
    #Define path, execute view function and give the name to this route for easy use(elsewhere)

    path("home/", views.home, name="home"),

    path("authors/", views.author_list, name="author_list"),
    path("authors/create/", views.author_create, name="author_create"),
    path("authors/<int:author_id>/", views.author_detail, name="author_detail"),
    path("authors/<int:author_id>/edit/", views.author_update, name="author_update"),
    path("authors/<int:author_id>/delete/", views.author_delete, name="author_delete"),
    

    path("books/", views.book_list, name="book_list"),
    path("books/create/", views.book_create, name="book_create"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("books/<int:book_id>/edit/", views.book_update, name="book_update"),
    path("books/<int:book_id>/delete/", views.book_delete, name="book_delete"),
    
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
    path("categories/<int:category_id>/", views.category_detail, name="category_detail"),
    path("categories/<int:category_id>/edit/", views.category_update, name="category_update"),
    path("categories/<int:category_id>/delete/", views.category_delete, name="category_delete"),
    
]