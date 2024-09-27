from django.db import models

class Fabricante(models.Model):
    nome = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        if self.nacionalidade:
            return f"{self.nome} ({self.nacionalidade})"
        else:
            return self.nome