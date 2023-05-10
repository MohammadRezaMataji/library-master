from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

def projects(request):
    Books = Book.objects.all()
    context = {'books':Books}
    return render(request,'project/projects.html', context)

def project(request,pk):
    bookObj = Book.objects.get(id= pk)
    return render(request,'project/project.html',{'book':bookObj})

def createbook(request):
    form = BookForm

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request,'project/book_form.html', context)

def updatebook(request,pk):
    book = Book.objects.get(id=pk )
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request,'project/book_form.html', context)

def deletebook(request, pk):
    book = Book.objects.get(id = pk)
    if request.method == 'POST':
        book.delete()
        return redirect('projects')
    context = {'object':book}
    return render(request, 'project/delete_template.html', context)