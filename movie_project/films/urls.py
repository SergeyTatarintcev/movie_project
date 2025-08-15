from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.list_films, name='list'),       # /films/
    path('add/', views.add_film, name='add'),      # /films/add/
]
