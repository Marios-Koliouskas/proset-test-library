from django import forms
from .models import Author, Book, Category

#Form thats based on a model (ModelForm)
class AuthorForm(forms.ModelForm):

    #Meta is an inside class so Django can understand in which model the form is based on and which fields will be displayed
    class Meta:

        #This form is for the Author model
        model = Author

        fields = ["first_name", "last_name", "birth_date", "description"]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =["title", "author", "pub_date", "category", "price", "description"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =["name", "description"]