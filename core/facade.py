import random


def create_contexto_lista():
    list_times_fifa17 = [
        "Bayern Munchen",
        "Chelsea",
        "Gamba Osaka",
        "Internazionale Milano",
        "Juventus",
        "Lyonnais",
        "Manchester City",
        "Manchester United",
        "PSG",
        "Real Madrid",
        "Seatle Sounders",
        "Tigres",
    ]
    return {"list_times_fifa17": list_times_fifa17}


def create_contexto_lista_sorteada(lista):
    lista_sorteada = random.shuffle(lista, len(lista))
    return {"lista_sorteada": lista_sorteada}