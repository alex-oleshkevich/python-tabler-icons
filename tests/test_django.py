import django
import os
import pytest
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.test import RequestFactory


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})


@pytest.fixture(autouse=True, scope='session')
def setup_django() -> None:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.django_app.settings'
    django.setup()


def test_renders_icons() -> None:
    factory = RequestFactory()
    request = factory.get('/')
    response = index_view(request)
    assert (
        response.content.decode().strip()
        == '<svg class="tabler-icon tabler-icon-user-check" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">\n  <path stroke="none" d="M0 0h24v24H0z" fill="none" />\n  <circle cx="9" cy="7" r="4" />\n  <path d="M3 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2" />\n  <path d="M16 11l2 2l4 -4" />\n</svg>'
    )
