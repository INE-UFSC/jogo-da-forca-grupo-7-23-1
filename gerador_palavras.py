import random

palavras = [
    "Amarelo",
    "Amiga",
    "Amor",
    "Ave",
    "Aviao",
    "Avo",
    "Balao",
    "Bebe",
    "Bolo",
    "Branco",
    "Cama",
    "Caneca",
    "Celular",
    "Ceu",
    "Clube",
    "Copo",
    "Doce",
    "Elefante",
    "Escola",
    "Estojo",
    "Faca",
    "Foto",
    "Garfo",
    "Geleia",
    "Girafa",
    "Janela",
    "Limonada",
    "Mae",
    "Meia",
    "Noite",
    "oculos",
    "onibus",
    "Ovo",
    "Pai",
    "Pao",
    "Parque",
    "Passarinho",
    "Peixe",
    "Pijama",
    "Rato",
    "Umbigo"
]


def escolhe_palavra():
        return palavras[random.randint(0, len(palavras)-1)].lower()