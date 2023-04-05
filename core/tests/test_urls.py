from django.urls import resolve, reverse

from core import views


def test_url_core():
    # Teste para a URL da view "gera_pagamentos" em core
    url = reverse("gera_pagamentos")
    resolver = resolve(url)
    assert resolver.view_name == "gera_pagamentos"
    assert resolver.func == views.gera_pagamentos
