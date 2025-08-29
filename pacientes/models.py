from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade_natal = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("view_own_paciente", "Can view own pacientes"),
        ]

    def __str__(self):
        return self.nome
