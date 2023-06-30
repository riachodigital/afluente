from afluente.customers.models import Customer


def test_if_customer_returns_name(db):
    customer = Customer.objects.create(
        name="Customer Inc", 
        responsible="Responsible", 
        email="test@customer.com", 
        phone="819999999"
        )
    assert customer.name == str(customer)
