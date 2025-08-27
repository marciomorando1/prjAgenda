from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.paciente_novo, name='paciente_novo'),
    path('lista/', views.paciente_lista, name='paciente_lista'),
    path('pacientes/<int:pk>/editar/', views.paciente_editar, name='paciente_editar'),
    path('pacientes/<int:pk>/excluir/', views.paciente_excluir, name='paciente_excluir'),
]
