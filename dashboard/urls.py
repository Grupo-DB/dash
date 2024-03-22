from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('dashboard_grupodb.urls')),
    path('', include('equipamentos.urls')),
    path('', include('britagem.urls')),
    path('', include('rebritagem.urls')),
    path('', include('fertilizantes.urls')),
    path('', include('cal.urls')),
    path('', include('argamassa.urls')),
    path('', include('calcario.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)