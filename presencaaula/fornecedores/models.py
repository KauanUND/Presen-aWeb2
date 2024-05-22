from django.db import models

# Create your models here.

class Fornecedor(models.Model):

    nome_empresa = models.CharField(max_length=200)
    nome_contato = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    produtos_fornecidos = models.TextField()
    