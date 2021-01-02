from django.db import models


class Service(models.Model):
    HOSPEDAGEM = 'HP'
    EMAIL = 'MA'
    NUVEM = 'NV'
    SERVICE_CHOICES = [
        (HOSPEDAGEM, 'Hospedagem'),
        (EMAIL, 'E-mail'),
        (NUVEM, 'Nuvem'),
    ]
    service = models.CharField(verbose_name='Serviço', max_length=2, choices=SERVICE_CHOICES, default=HOSPEDAGEM)
    begin_date = models.DateField(verbose_name='Início do Serviço')
    end_date = models.DateField(verbose_name='Término do Serviço')
    price = models.DecimalField(verbose_name="Valor", decimal_places=2, max_digits=4)
    observation = models.TextField(verbose_name="Observações", blank=True, null=True)
