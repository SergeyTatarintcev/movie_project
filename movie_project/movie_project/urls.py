from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include('films.urls', namespace='films')),
    path('', RedirectView.as_view(pattern_name='films:list', permanent=False)),  # редирект с / на /films/
]
