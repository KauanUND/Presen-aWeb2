from django.db import models

# Create your models here.

class Funcionario(models.Model):

    nome_completo = models.CharField(max_length=200)
    cargo = models.CharField(max_length=100)
    email_corporativo = models.EmailField()
    departamento = models.CharField(max_length=100)
    data_admissao = models.DateField()