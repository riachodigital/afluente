from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.urls import reverse

from afluente.demo.forms import ClienteForm
from afluente.demo.models import Cliente


def index(request):
    query_set = Cliente.objects.order_by('nome')
    ctx = {
        'demo': list(query_set)
    }
    return render(request, 'demo/index.html', context=ctx)


@login_required
def new(request):
    ctx = {'form': ClienteForm()}
    return render(request, 'demo/client_form.html', context=ctx)


@login_required
def create(request):
    # Extrair dados do request
    form = ClienteForm(request.POST, request.FILES)
    # Validar os inputs
    if not form.is_valid():
        ctx = {'form': form}
        return render(request, 'demo/client_form.html', context=ctx, status=400)
    # Se válido, salvar no banco e redirecionar
    form.save()
    return redirect(reverse('demo:index'))
