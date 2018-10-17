import pytest
from django.urls import reverse
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


def test_status_code_user_not_logged(resp_without_user):
    assert resp_without_user.url.startswith(reverse('login'))


def test_status_code_user_logged(resp):
    assert resp.url.startswith(reverse('demo:index'))


def test_cliente_salvo(resp):
    assert Cliente.objects.exists()
