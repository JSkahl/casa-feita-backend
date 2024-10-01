from django.db import models
from django.core.validators import MaxValueValidator

from .produto import Produto
from .usuario import Usuario

class Endereco(models.Model):
    rua = models.CharField(max_length=150)
    complemento = models.CharField(max_length=150)
    numero = models.IntegerField(validators=[MaxValueValidator(999)])
    cep = models.IntegerField(validators=[MaxValueValidator(99999999)])

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        CONCLUIDA = 2, "Concluida"
        PREPARACAO = 3, "Preparação"
        SAIDA = 4, "Saída"
        ENTREGUE = 5, "Entregue"

    class MetodoPagamento(models.IntegerChoices):
        CARTAO_CREDITO = 1, "Cartão de crédito"
        CARTAO_DEBITO = 2, "Cartão de débito"
        PIX = 3, "Pix"
        BOLETO = 4, "Boleto"

    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    metodo_pagamento = models.IntegerField(choices=MetodoPagamento.choices)
    data = models.DateField(auto_now_add=True)

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="compras")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="produtos")
    quantidade = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Item Compra"
        verbose_name_plural = "Itens da Compra"