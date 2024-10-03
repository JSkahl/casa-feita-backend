from django.db import models

from uploader.models import Image

class Fabricante(models.Model):
    nome = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=50)
    logo = models.ForeignKey(Image,related_name="+", on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        if self.nacionalidade:
            return f"{self.nome} ({self.nacionalidade})"
        else:
            return self.nome