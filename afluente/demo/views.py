from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from django.http import HttpResponse
from django.urls import reverse

from afluente.demo.models import Cliente


def index(request):
    query_set = Cliente.objects.order_by('nome')
    ctx = {
        'demo': list(query_set)
    }
    return render(request, 'demo/index.html', context=ctx)


@login_required
def new(request):
    return render(request, 'demo/client_form.html')


@login_required
def create(request):
    dct = request.GET
    cliente = Cliente(nome=dct['nome'], status=dct['status'], servico=dct['servico'])
    cliente.save()
    return redirect(reverse('demo:index'))
