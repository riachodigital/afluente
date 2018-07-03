from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    servico = models.CharField(max_length=50)
