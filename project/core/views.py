#Recieves an HTML template, it fills it with data and returns a page to the browser
from django.shortcuts import render, get_object_or_404, redirect

from .models import Author, Book, Category

from .forms import AuthorForm, BookForm, CategoryForm

# Create your views here.

#A python function thats being called when someone opens the specific url
#The request is the request of the user/browser
def author_list(request):
    #Bring every author from the database
    authors = Author.objects.all().order_by("-id")
    #Open the HTML file author_list.html and send the variable authors
    return render(request, "core/author_list.html", {"authors": authors})
    
def author_detail(request, author_id):
    #Take author with the id given or 404 page
    author = get_object_or_404(Author, id = author_id)
    return render(request, "core/author_detail.html", {"author": author})

def author_create(request):
    # This view handles the creation of a new Author.

    # If the request method is POST, it means that the user submitted the form.
    # So the browser is sending the filled form data to the server.
    if request.method == "POST":

        # Create an AuthorForm object using the submitted data.
        # request.POST contains the data that the user typed in the form.
        form = AuthorForm(request.POST)

        # Check if the submitted data is valid according to the Author model rules.
        # For example: required fields must not be empty.
        if form.is_valid():

            # If the form is valid, save the new Author object to the database.
            form.save()

            # After saving, redirect the user back to the authors list page.
            return redirect("author_list")

    else:
        # If the request method is GET, it means that the user just opened the page.
        # So we create an empty form to display it.
        form = AuthorForm()

    # Render the HTML template and pass the form to it.
    # The template will use {{ form.as_p }} to display the form fields.
    return render(request, "core/author_form.html", {"form": form})

def author_update(request, author_id):
    # Find the author we want to edit, using the id from the URL.
    # If no author with this id exists, show 404 page.
    author = get_object_or_404(Author, id=author_id)

    # If the user submitted the form, we receive a POST request.
    if request.method == "POST":

        # Create a form with the submitted data.
        # instance=author means:
        # update this existing author, do not create a new one.
        form = AuthorForm(request.POST, instance=author)

        # Check if the submitted data is valid.
        if form.is_valid():

            # Save the changes to the existing author in the database.
            form.save()

            # After saving, go to the detail page of this author.
            return redirect("author_detail", author_id=author.id)

    else:
        # If it is a GET request, the user just opened the edit page.
        # Create a form filled with the existing author's data.
        form = AuthorForm(instance=author)

    # Render the same form template and pass the form to the HTML.
    return render(request, "core/author_form.html", {"form": form})

def book_list(request):
    books = Book.objects.all().order_by("-id")
    return render(request, "core/book_list.html", {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    return render(request, "core/book_detail.html", {"book": book})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "core/book_form.html", {"form": form})

def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, "core/book_form.html", {"form": form})

def category_list(request):
    categories = Category.objects.all().order_by("-id")
    return render(request, "core/category_list.html", {"categories": categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    return render(request, "core/category_detail.html", {"category": category})

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("category_list")
    else:
        form = CategoryForm()
    return render(request, "core/category_form.html", {"form": form})

def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            return redirect("category_detail", category_id = category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, "core/category_form.html", {"form": form})


