from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('temperature', views.city, name='city')
]