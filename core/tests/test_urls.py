from django.urls import resolve, reverse

from core import views


def test_url_index_core():
    # Teste para a URL da view "gera_pagamentos" em core
    url = reverse("index_core")
    resolver = resolve(url)
    assert resolver.view_name == "index_core"
    assert resolver.func == views.index_core

def test_url_gera_campeonato():
    # Teste para a URL da view "gera_pagamentos" em core
    url = reverse("gera_campeonato")
    resolver = resolve(url)
    assert resolver.view_name == "gera_campeonato"
    assert resolver.func == views.gera_campeonato
