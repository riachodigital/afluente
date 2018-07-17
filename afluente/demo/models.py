from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    servico = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f'Cliente(nome="{self.nome}", status="{self.status}", servico="{self.servico}"'
