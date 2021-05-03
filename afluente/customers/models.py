from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    responsible = models.CharField(max_length=200, verbose_name="Responsável")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=11, verbose_name="Telefone")
    is_active = models.BooleanField(default=True, verbose_name="Ativa")

    def __str__(self):
        return self.name
