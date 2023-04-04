import random

from django.http import JsonResponse
from django.template.loader import render_to_string


def create_contexto_lista():
    list_times_fifa17 = [
        {"time": "Bayern Munchen", "logo": "bayern"},
        {"time": "Chelsea", "logo": "chelsea"},
        {"time": "Gamba Osaka", "logo": "gamba"},
        {"time": "Internazionale Milano", "logo": "inter"},
        {"time": "Juventus", "logo": "juventus"},
        {"time": "Lyonnais", "logo": "lyon"},
        {"time": "Manchester City", "logo": "city"},
        {"time": "Manchester United", "logo": "united"},
        {"time": "PSG", "logo": "psg"},
        {"time": "Real Madrid", "logo": "real"},
        {"time": "Seattle Sounders", "logo": "sounders"},
        {"time": "Tigres", "logo": "tigres"},
    ]
    return {"list_times_fifa17": list_times_fifa17}


def create_contexto_lista_sorteada():
    lista = create_contexto_lista()
    lista_sorteada = random.shuffle(lista, len(lista))
    return {"lista_sorteada": lista_sorteada}


def create_data_tabela_campeonato(request, contexto):
    data = dict()
    html_tabela_campeonato(request, contexto, data)
    return JsonResponse(data)


def html_tabela_campeonato(request, contexto, data):
    data["html_tabela_campeonato"] = render_to_string(
        "core/html_tabela_campeonato.html", contexto, request=request
    )
    return data
