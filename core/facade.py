import random


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
