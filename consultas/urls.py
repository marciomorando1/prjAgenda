from django.urls import path
from . import views

urlpatterns = [
    path('nova/', views.consulta_nova, name='consulta_nova'),
    path('lista/', views.consulta_lista, name='consulta_lista'),
    path('editar/<int:pk>/', views.consulta_editar, name='consulta_editar'),
    path('calendario/', views.calendario, name='calendario'),
]

