from django.urls import resolve, reverse

from core import views


def test_url_core():
    # Teste para a URL da view "gera_pagamentos" em core
    url = reverse("index_core")
    resolver = resolve(url)
    assert resolver.view_name == "index_core"
    assert resolver.func == views.index_core
