# 🎬 movie_project — Django mini‑приложение фильмов

Небольшой учебный проект на **Django 5** (Python 3.11+): форма добавления фильма и страница со списком фильмов из базы данных.

## 🚀 Функционал
- Приложение **films** с моделью `Film(title, description, review)`
- Страница **добавления** фильма (форма, валидация)
- Страница **списка** фильмов (вывод последних добавленных)
- Админка (опционально): просмотр/редактирование записей

## 📦 Требования
- Python 3.11+
- Django 5.x

## 🔧 Установка и запуск (Windows PowerShell / macOS / Linux)
```bash
# 1) Клонирование
git clone <ВАШ_РЕПОЗИТОРИЙ>.git
cd movie_project

# 2) Виртуальное окружение
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS / Linux
# source .venv/bin/activate

# 3) Зависимости
pip install django

# 4) Миграции БД
python manage.py makemigrations
python manage.py migrate

# 5) (Опционально) суперпользователь для /admin
python manage.py createsuperuser

# 6) Старт dev-сервера
python manage.py runserver
```

Откройте:
- Форма добавления: **http://127.0.0.1:8000/add/** или **/films/add/** (зависит от urls, см. ниже)
- Список фильмов: **http://127.0.0.1:8000/** или **/films/**

## 🧩 Структура проекта (основное)
```
movie_project/
├─ films/
│  ├─ migrations/
│  ├─ templates/films/
│  │  ├─ add.html      # форма добавления
│  │  └─ list.html     # список фильмов
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ urls.py
│  └─ views.py
├─ movie_project/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ manage.py
└─ README.md
```

## 🧱 Модель
`films/models.py`
```python
from django.db import models

class Film(models.Model):
    title = models.CharField('Название фильма', max_length=200)
    description = models.TextField('Описание фильма')
    review = models.TextField('Отзыв')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-id']
```

## ✍️ Форма
`films/forms.py`
```python
from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('title', 'description', 'review')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв'}),
        }
```

## 🖥 Вьюхи
`films/views.py`
```python
from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films:list')
    else:
        form = FilmForm()
    return render(request, 'films/add.html', {'form': form})

def list_films(request):
    films = Film.objects.all()
    return render(request, 'films/list.html', {'films': films})
```

## 🔗 Маршруты
`movie_project/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Вариант A: список фильмов — главная страница
    path('', include('films.urls', namespace='films')),
    # Вариант B: если хотите оставить префикс /films/:
    # path('films/', include('films.urls', namespace='films')),
]
```

`films/urls.py`
```python
from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.list_films, name='list'),   # /  или /films/
    path('add/', views.add_film, name='add'),  # /add/ или /films/add/
]
```

## 🧪 Быстрая проверка
1. Откройте страницу **добавления** → заполните 3 поля → отправьте.
2. Вас перекинет на **список**, где появится новая запись.
3. Зайдите в **/admin/**, чтобы убедиться, что данные действительно в БД.

## 🗂 Рекомендованный .gitignore
`/.gitignore`
```
# Python/Django
__pycache__/
*.py[cod]
*.egg-info/
db.sqlite3

# Виртуальное окружение
.venv/
venv/
env/

# IDE
.vscode/
.idea/
```

## ⚙️ Полезно знать
- Для корректной локали/часового пояса:
  ```python
  # settings.py
  LANGUAGE_CODE = 'ru'
  TIME_ZONE = 'Europe/Moscow'
  USE_TZ = True
  ```
- На Windows поставьте базу часовых поясов: `pip install tzdata`.

---

Готово! 

** Сделано [SergeyTatarintcev](https://github.com/SergeyTatarintcev) 
