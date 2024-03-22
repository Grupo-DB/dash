from django.urls import path
from . import views

urlpatterns = [
    path('argamassa', views.home_argamassa, name="home_argamassa"),
    
]