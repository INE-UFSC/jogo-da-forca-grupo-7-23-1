#gerencia o estado do jogo #Responsavel: Casotti

import random
from gerador_palavras import escolhe_palavra

class Computador:
    def __init__(self,palavra):
        self.palavra = palavra

    def tamanho_palavra(self):
        """@return tamanho da palavra"""

        return len(self.palavra)

    def tentar_letra(self, letra, palavra_mostrar):
        """@return se a letra existe na palavra"""
        acertou = False
        for i in range(len(self.palavra)):
            if self.palavra[i] == letra:
                palavra_mostrar[i] = letra 
                acertou = True
        
        return acertou

    def ganhou(self):
        self.palavra = ''

