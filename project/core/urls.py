from django.urls import path
from . import views

#When someone visits authors/, execute the author_list view
urlpatterns = [
    #Define path, execute view function and give the name to this route for easy use(elsewhere)
    path("authors/", views.author_list, name="author_list"),
    path("books/", views.book_list, name="book_list"),
    path("categories/", views.category_list, name="category_list"),
]