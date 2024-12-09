from django.db import models
from django.contrib.auth.models import User

class Estudante(models.Model):
    # Relacionamento um-para-um com o modelo User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    conquistas = models.IntegerField(blank=True, null=True) 
    tipo_plano = models.CharField(max_length=50, choices=[('EDUCABASIC', 'EDUCAULTRA')])

