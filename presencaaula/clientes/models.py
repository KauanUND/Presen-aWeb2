from django.db import models

# Create your models here.

class Cliente (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    cpf = models.CharField(max_length=18)