from django.urls import path
from . import views

#When someone visits authors/, execute the author_list view
urlpatterns = [
    path("authors/", views.author_list, name="author_list"),
    path("books/", views.book_list, name="book_list"),
]