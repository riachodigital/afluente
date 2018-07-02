from django.shortcuts import render

# from django.http import HttpResponse
from afluente.demo.models import Cliente


def index(request):
    ctx = {
        'demo':
            [
                Cliente(
                    'Cliente 1',
                    'Ativo',
                    'Hospedagem'
                ),
                Cliente(
                    'Cliente 2',
                    'Inativo',
                    'E-mail'
                ),
                Cliente(
                    'Nasa',
                    'Inativo',
                    'Hospedagem'
                )
            ]
    }
    return render(request, 'demo/index.html', context=ctx)
