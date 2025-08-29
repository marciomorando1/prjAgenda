from django.db import models
from pacientes.models import Paciente
from django.contrib.auth.models import User

class Consulta(models.Model):
    SITUACAO_CHOICES = [
        ('Em aberto', 'Em aberto'),
        ('Finalizada', 'Finalizada')
    ]

    TIPO_CHOICES = [
        ('Plano de Saude', 'Plano de Saude'),
        ('Particular', 'Particular')
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_consulta = models.DateField()
    valor_consulta = models.DecimalField(max_digits=10, decimal_places=2)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES, default='Em aberto')
    tipo_consulta = models.CharField(max_length=20, choices=TIPO_CHOICES, default='Particular')

    def __str__(self):
        return f"{self.id} - {self.paciente.nome}"
