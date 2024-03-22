from django.urls import path
from . import views

urlpatterns = [
    path('detalha', views.home_britagem, name="home_britagem"),
    
]