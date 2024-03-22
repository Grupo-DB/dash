from django.urls import path
from . import views

urlpatterns = [
    path('cal', views.home_cal, name="home_cal"),
    
]