from django.db import models

from .categoria import Categoria
from .cor import Cor
from .fabricante import Fabricante

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="categorias")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="cores")
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.cor}) | R${self.preco} | {self.quantidade} em estoque."