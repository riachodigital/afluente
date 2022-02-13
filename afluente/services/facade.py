from datetime import date, timedelta

from django.utils import timezone

from afluente.services.models import Service


def list_services_that_expire_this_month():
    month = timezone.now()
    return list(Service.objects.filter(end_date__month=month.month, end_date__year=month.year))


def list_services_that_expire_next_month():
    month = date.today()
    next_month = month + timedelta(days=30)
    return list(Service.objects.filter(end_date__month=next_month.month, end_date__year=month.year))
