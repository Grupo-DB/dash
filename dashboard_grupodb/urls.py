from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.home, name="home"),
    path('mes', views.mensal, name="mensal"),
    path('ano', views.anual, name="anual"),
    path('/producao',views.prod_ini, name="prod_ini"),
    path('/detalha_calcario',views.det_calcario, name="det_calcario"),
    path('../equipamentos/',include('equipamentos.urls')),
    path('../britagem/',include('britagem.urls'))
]