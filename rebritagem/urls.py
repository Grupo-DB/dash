from django.urls import path
from . import views

urlpatterns = [
    path('rebritagem', views.home_rebritagem, name="home_rebritagem"),
    
]