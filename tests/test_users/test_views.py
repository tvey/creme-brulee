import pytest

from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from users.views import token_generator

pytestmark = [pytest.mark.django_db(transaction=True)]

register_path = reverse('users:register')
login_path = reverse('users:login')
homepage = reverse('home')


def activate_path(user):
    token = token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    params = {'uidb64': uid, 'token': token}
    path = reverse('users:activate-account', kwargs=params)
    return path


def test_register_view_is_ok(client):
    response = client.get(register_path)
    assert response.status_code == 200


def test_register_view_redirects_authenticated_user(client, new_user):
    client.force_login(new_user())
    response = client.get(register_path)
    assert response.status_code == 302
    assert response.url == homepage


def test_activate_account_view_redirects_authenticated_user(client, new_user):
    user = new_user()
    path = activate_path(user)
    client.force_login(user)
    response = client.get(path)
    assert response.status_code == 302
    assert response.url == homepage


def test_login_view_is_ok(client):
    response = client.get(login_path)
    assert response.status_code == 200


def test_login_view_redirect_authenticated_user(client, new_user):
    client.force_login(new_user())
    response = client.get(login_path)
    assert response.status_code == 302
    assert response.url == homepage


def test_login_active_user_with_username(client, new_user, password_fix):
    user = new_user(password=password_fix)
    logged_in = client.login(username=user.username, password=password_fix)
    assert logged_in


def test_login_active_user_with_email(client, new_user, password_fix):
    user = new_user(password=password_fix)
    logged_in = client.login(username=user.email, password=password_fix)
    assert logged_in


def test_logout_view(client, new_user):
    path = reverse('users:logout')
    client.force_login(new_user())
    response = client.get(path)
    assert response.status_code == 302
    assert response.url == homepage


def test_logout_view_redirect_anonymous_user(client):
    path = reverse('users:logout')
    response = client.get(path)
    assert response.status_code == 302
    assert response.url == homepage


def test_change_password_view_redirects_anonymous_user(client):
    path = reverse('users:change-password')
    response = client.get(path)
    assert response.status_code == 302
    assert 'login' in response.url
    assert 'next' in response.url
    assert 'change-password' in response.url
