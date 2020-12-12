from django.db import models


class Customer(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    responsavel = models.CharField(max_length=200, verbose_name="Responsável")
    email = models.EmailField(verbose_name="E-mail")
    fone = models.CharField(max_length=11, verbose_name="Telefone")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return self.nome
