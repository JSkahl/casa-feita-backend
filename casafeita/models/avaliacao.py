from django.db import models

class Avaliacao(models.Model):
    conteudo = models.CharField(max_length=255, blank=True, null=True)
    ranking = models.CharField(max_length=1)
    data = models.DateField()

    def __str__(self):
        return self.ranking