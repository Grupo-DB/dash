from django.urls import path
from . import views

urlpatterns = [
    path('calcario', views.home_calcario, name="home_calcario"),
    
]