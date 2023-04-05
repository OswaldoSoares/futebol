from django.urls import path

from core.views import gera_campeonato, index_core

urlpatterns = [
    path(
        "",
        index_core,
        name="index_core",
    ),
    path(
        "gera_campeonato/",
        gera_campeonato,
        name="gera_campeonato",
    ),
]
