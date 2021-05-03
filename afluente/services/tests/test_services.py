from dateutil.relativedelta import relativedelta
from django.utils import timezone

from afluente.customers.models import Customer
from afluente.services.models import Service


def test_service_and_customer_relationship(db):
    today = timezone.now().date()
    next_year = today + relativedelta(years=1)
    customer = Customer.objects.create(name="Test")
    service = Service.objects.create(
        service='HP',
        customer=customer,
        begin_date=today,
        end_date=next_year,
        price=100
    )
    assert service.customer == customer
