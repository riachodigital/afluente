import pytest
from django.urls import reverse

from afluente.demo.forms import ClienteForm
from afluente.demo.models import Cliente


@pytest.fixture
def resp_without_user(client: Cliente):
    return client.post(
        reverse('demo:create'), data={
            'nome': 'Nasa',
            'status': 'AT',
            'servico': 'HOSP',
        })


@pytest.fixture
def user(django_user_model):
    user = django_user_model(name='Isaac')
    user.save()
    return user


@pytest.fixture
def resp(user, client: Cliente):
    client.force_login(user)
    return resp_without_user(client)


@pytest.fixture
def resp_no_data(user, client: Cliente):
    client.force_login(user)
    return client.post(
        reverse('demo:create'), data={
            'nome': '',
            'status': '',
            'servico': '',
        })


def test_status_code_user_not_logged(resp_without_user):
    assert resp_without_user.url.startswith(reverse('login'))


# def test_status_code_user_logged(resp):
#     assert resp.url.startswith(reverse('demo:index'))


# def test_cliente_salvo(resp):
#     assert Cliente.objects.exists()


def test_status_code_for_error(resp_no_data):
    assert 400 == resp_no_data.status_code


def test_status_invalid_date_in_context(resp_no_data):
    assert isinstance(resp_no_data.context['form'], ClienteForm)
