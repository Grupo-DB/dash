from django.urls import path
from . import views

urlpatterns = [
    path('fertilizantes', views.home_fertilizantes, name="home_fertilizantes"),
    
]