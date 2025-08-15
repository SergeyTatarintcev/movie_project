from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films:list')  # после сохранения идём на страницу списка
    else:
        form = FilmForm()
    return render(request, 'films/add.html', {'form': form})

def list_films(request):
    films = Film.objects.all()
    return render(request, 'films/list.html', {'films': films})
