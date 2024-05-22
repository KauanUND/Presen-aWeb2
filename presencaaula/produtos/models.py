from django.db import models

# Create your models here.

class Produtos(models.Model):

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    categoria = models.CharField(max_length=100)
    quantidade_estoque = models.IntegerField()
