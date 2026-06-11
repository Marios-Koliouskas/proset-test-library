from django.urls import path
from . import views

#When someone visits authors/, execute the author_list view
urlpatterns = [
    #Define path, execute view function and give the name to this route for easy use(elsewhere)
    path("authors/", views.author_list, name="author_list"),
    path("authors/<int:author_id>/", views.author_detail, name="author_detail"),

    path("books/", views.book_list, name="book_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    
    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:category_id>/", views.category_detail, name="category_detail"),
]