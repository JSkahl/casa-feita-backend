from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .produto import Produto
from .usuario import Usuario
from uploader.models import Image

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)
    rating = models.DecimalField(decimal_places=1, max_digits=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0)
    data = models.DateField(auto_now_add=True)
    foto = models.ForeignKey(Image, related_name="+", on_delete=models.SET_NULL, blank=True, null=True, default=None)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
        
    def __str__(self):
        return f"Avaliação: {self.rating} | Postado: {self.data}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural= "Avaliações"