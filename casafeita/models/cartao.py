from django.db import models
from django.core.validators import MaxValueValidator

class Cartao(models.Model):
    class TipoCartao(models.TextChoices):
        DEBITO = "Débito"
        CREDITO = "Crédito"

    nome_titular = models.CharField(max_length=255)
    sobrenome_titular = models.CharField(max_length=255)
    numero = models.IntegerField(validators=[MaxValueValidator(9999999999999999)])
    validade = models.DateField()
    cvv = models.IntegerField(validators=[MaxValueValidator(999)])
    tipo = models.CharField(max_length=10, choices=TipoCartao.choices)

    class Meta:
        verbose_name = "Cartão"
        verbose_name_plural = "Cartões"

    def __str__(self):
        return f"{self.nome_titular} {self.sobrenome_titular} | {self.tipo}"