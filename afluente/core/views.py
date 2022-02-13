# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from afluente.services.facade import list_services_that_expire_this_month, list_services_that_expire_next_month


def home(request):
    return render(request, 'core/home.html')


@login_required
def dashboard(request):
    expire_this_month = list_services_that_expire_this_month()
    expire_next_month = list_services_that_expire_next_month()
    return render(request, 'core/dashboard.html',
                  {'expires_this_month': expire_this_month, 'expires_next_month': expire_next_month})

def contato(request):
    return render(request, 'core/contato.html')
