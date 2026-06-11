#Recieves an HTML template, it fills it with data and returns a page to the browser
from django.shortcuts import render

from .models import Author, Book, Category

# Create your views here.

#A python function thats being called when someone opens the specific url
#The request is the request of the user/browser
def author_list(request):
    #Bring every author from the database
    authors = Author.objects.all()
    #Open the HTML file author_list.html and send the variable authors
    return render(request, "core/author_list.html", {"authors": authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, "core/book_list.html", {"books": books})

def category_list(request):
    categories = Category.objects.all()
    return render(request, "core/category_list.html", {"categories": categories})
