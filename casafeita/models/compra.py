from django.db import models

class Compra(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)

class Endereco(models.Model):
    rua = models.CharField(max_length=150)
    numero = models.IntegerField(max_length=10)
    complemento = models.CharField(max_length=150)
    cep = models.IntegerField(max_length=20)

    