from django.contrib import admin
from django.urls import path, include
from consultas.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Página inicial com calendário
    path('pacientes/', include('pacientes.urls')),
    path('consultas/', include('consultas.urls')),
]
