from django.urls import path
from . import views

urlpatterns = [
    path('detalhe', views.home_eqps, name="home_eqps"),
    path('data', views.get_data, name='get_data'),
]