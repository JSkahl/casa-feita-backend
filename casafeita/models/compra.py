from django.db import models

from .produto import Produto

class Endereco(models.Model):
    rua = models.CharField(max_length=150)
    numero = models.IntegerField(max_length=10)
    complemento = models.CharField(max_length=150)
    cep = models.IntegerField(max_length=20)

class Cartao(models.Model):
    numero = models.IntegerField(max_length=16)
    nome = models.CharField(max_length=150)
    validade = models.DateField()
    cvv = models.IntegerField(max_length=3)

class Compra(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    cartao = models.ForeignKey(Cartao, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.item.produto.nome} | {self.item.quantidade} unidades."

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="compras")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="produtos")
    quantidade = models.IntegerField(max_length=10)