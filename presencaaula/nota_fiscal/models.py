from django.db import models

# Create your models here.
class NotaFiscal (models.Model):

    numero = models.CharField(max_length=20, unique=True)
    data_emissao = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    nome_cliente = models.CharField(max_length=200)
    descricao_itens = models.TextField()