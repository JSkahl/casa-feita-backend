from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)
    rating = models.DecimalField(decimal_places=1, max_digits=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação: {self.rating} | Postado: {self.data}"