from django.db import models


class Cliente(models.Model):

    status_choice = (
        ('AT', 'Ativo'),
        ('INT', 'Inativo'),
    )
    servico_choice = (
        ('HOSP', 'Hospedagem'),
        ('MAIL', 'E-mail'),
        ('HOSMAIL', 'Hospedagem e E-mail'),
    )
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=status_choice)
    servico = models.CharField(max_length=51, choices=servico_choice)
    imagem = models.ImageField(max_length=200, upload_to='clientes/', null=True)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f'Cliente(nome="{self.nome}", status="{self.status}", servico="{self.servico}"'
