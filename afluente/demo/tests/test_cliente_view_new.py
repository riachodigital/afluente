import pytest
from django.urls import reverse

# from afluente.demo.models import Cliente
# from afluente.django_assertions import dj_assert_contains


@pytest.fixture
def resp_without_user(client):
    return client.get(reverse('demo:new'))


@pytest.fixture
def user(django_user_model):
    user = django_user_model(name='Isaac')
    user.save()
    return user


# @pytest.fixture
# def resp(user, client: Cliente):
#     client.force_login(user)
#     return resp_without_user(client)

# @pytest.fixture
# def resp(client):
#     return _resp(client)
#
#
# def _resp(client):
#     client.force_login(user)
#     return resp_without_user(client)
#
#
# def test_status_code_user_not_logged(resp_without_user):
#     assert 302 == resp_without_user.status_code
#
#
# def test_status_code_user_logged(resp):
#     assert 200 == resp.status_code
#
#
# @pytest.mark.parametrize(
#     'content', [
#         '<input type="text" name="nome"',
#         '<option value="AT">Ativo</option>',
#         '<option value="INT">Inativo</option>',
#         '<option value="HOSP">Hospedagem</option>',
#         '<option value="MAIL">E-mail</option>',
#         '<option value="HOSPMAIL">Hospedagem e E-mail</option>',
#         '<button type="submit"',
#         'csrfmiddlewaretoken',
#     ]
# )
# def test_client_form_inputs(resp, content):
#     dj_assert_contains(resp, content)
#
#
# def test_client_form_action(resp):
#     dj_assert_contains(resp, f'''<form method="post" action="{reverse('demo:create')}''')
