#gerencia o estado do jogo #Responsavel: Casotti

import random

class Computador:
    def __init__(self):
        self.palavra = "aviao"

    def tamanho_palavra(self):
        """@return tamanho da palavra"""

        return len(self.palavra)

    def tentar_letra(self, letra, palavra_mostrar):
        """@return se a letra existe na palavra"""
        acertou = False
        #num_letras = self.palavra.count(letra)
        for i in range(len(self.palavra)):
            if self.palavra[i] == letra:
                palavra_mostrar[i] = letra 
                acertou = True
        #self.palavra.replace(letra, '')

        #return num_letras > 0
        return acertou

    def ganhou(self):
        self.palavra = ''

palavras = [
    "Amarelo",
    "Amiga",
    "Amor",
    "Ave",
    "Avião",
    "Avó",
    "Balão",
    "Bebê",
    "Bolo",
    "Branco",
    "Cama",
    "Caneca",
    "Celular",
    "Céu",
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
    "Mãe",
    "Meia",
    "Noite",
    "Óculos",
    "ônibus",
    "Ovo",
    "Pai",
    "Pão",
    "Parque",
    "Passarinho",
    "Peixe",
    "Pijama",
    "Rato",
    "Umbigo"
]

def escolhe_palavra():
    return palavras[random.randint(0, len(palavras)-1)]
