from django.db import models

from afluente.customers.models import Customer


class Service(models.Model):
    HOSPEDAGEM = 'HP'
    EMAIL = 'MA'
    HOSPEDAGEM_EMAIL = 'HE'
    NUVEM = 'NV'
    SERVICE_CHOICES = [
        (HOSPEDAGEM, 'Hospedagem'),
        (EMAIL, 'E-mail'),
        (HOSPEDAGEM_EMAIL, 'Hospedagem + E-mail'),
        (NUVEM, 'Nuvem'),
    ]
    service = models.CharField(
        verbose_name='Serviço',
        max_length=2,
        choices=SERVICE_CHOICES,
        default=HOSPEDAGEM,
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True
    )
    begin_date = models.DateField(verbose_name='Início do Serviço')
    end_date = models.DateField(verbose_name='Término do Serviço')
    price = models.DecimalField(
        verbose_name='Valor', decimal_places=2, max_digits=6
    )
    observation = models.TextField(
        verbose_name='Observações', blank=True, null=True
    )
