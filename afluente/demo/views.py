from django.shortcuts import render

# from django.http import HttpResponse
from afluente.demo.models import Cliente


def index(request):
    query_set = Cliente.objects.order_by('nome')
    ctx = {
        'demo': list(query_set)
    }
    return render(request, 'demo/index.html', context=ctx)
