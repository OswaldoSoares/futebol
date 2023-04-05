from django.shortcuts import render

from core import facade


def index_core(request):
    contexto = facade.create_contexto_lista()
    return render(request, "core/index.html", contexto)


def gera_campeonato(request):
    contexto = facade.create_contexto_lista_sorteada()
    data = facade.create_data_tabela_campeonato(request, contexto)
    return data
