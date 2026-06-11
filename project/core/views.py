#Recieves an HTML template, it fills it with data and returns a page to the browser
from django.shortcuts import render, get_object_or_404

from .models import Author, Book, Category

# Create your views here.

#A python function thats being called when someone opens the specific url
#The request is the request of the user/browser
def author_list(request):
    #Bring every author from the database
    authors = Author.objects.all()
    #Open the HTML file author_list.html and send the variable authors
    return render(request, "core/author_list.html", {"authors": authors})
    
def author_detail(request, author_id):
    #Take author with the id given or 404 page
    author = get_object_or_404(Author, id = author_id)
    return render(request, "core/author_detail.html", {"author": author})

def book_list(request):
    books = Book.objects.all()
    return render(request, "core/book_list.html", {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    return render(request, "core/book_detail.html", {"book": book})

def category_list(request):
    categories = Category.objects.all()
    return render(request, "core/category_list.html", {"categories": categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    return render(request, "core/category_detail.html", {"category": category})

