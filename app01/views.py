from django.shortcuts import render
from django.shortcuts import render,redirect

# Create your views here.

from .models import *

# Create your views here.
'''传统模式的增删改
def books(request):
    book_list=Book.objects.all()
    return render(request,"book.html",locals())

def addbook(request):

    if request.method=="POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish_id = request.POST.get("publish_id")
        author_pk_list = request.POST.get("author_pk_list")
        book_obj = Book.objects.create(title=title, price=price, date=date, publish_id=publish_id)
        book_obj.authors.add(*author_pk_list)
        return redirect("/books/")




    publish_list = Publish.objects.all()
    authors_list = Author.objects.all()
    return render(request,"add.html",locals())

def editbook(request,edit_book_id):
    if request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        date=request.POST.get("date")
        publish_id=request.POST.get("publish_id")
        author_pk_list=request.POST.getlist("author_pk_list") # [1,2]

        Book.objects.filter(pk=edit_book_id).update(title=title,price=price,date=date,publish_id=publish_id)
        book_obj=Book.objects.filter(pk=edit_book_id).first()
        book_obj.authors.set(author_pk_list)


        return redirect("/books/")



    edit_book=Book.objects.filter(pk=edit_book_id).first()
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request,"edit.html",locals())
    
'''
from django.forms import ModelForm
from django.forms import widgets as wid
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        labels = {"title":"书籍名称","price":"价格"}
        widgets = {
            "title": wid.TextInput(attrs={"class": "form-control"}),
            "price": wid.TextInput(attrs={"class": "form-control"}),
            "date": wid.TextInput(attrs={"class": "form-control", "type": "date"}),
            "publish": wid.Select(attrs={"class": "form-control"}),
            "authors": wid.SelectMultiple(attrs={"class": "form-control"}),
        }
        error_messages = {
            "title":{"required":"不能为空"}
        }

def books(request):
    book_list=Book.objects.all()
    return render(request,"book.html",locals())

def addbook(request):
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/books/")
        else:
            return render(request,"add.html",locals())
    form = BookForm()
    return render(request,"add.html",locals())

def editbook(request,edit_book_id):
    edit_book = Book.objects.filter(pk=edit_book_id).first()
    if request.method == "POST":
        form = BookForm(request.POST, instance=edit_book)
        if form.is_valid():
            form.save()  # edit_book.update(request.POST)
            return redirect("/books/")

    form = BookForm(instance=edit_book)
    return render(request, "edit.html", locals())









