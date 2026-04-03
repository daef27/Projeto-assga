from django.db import models

class Socio(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome