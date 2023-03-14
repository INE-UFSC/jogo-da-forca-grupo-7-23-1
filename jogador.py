# gerencia as açoes do jogador #Responsavel: Girotto

class Jogador:
    def __init__(self,vidas,letras_usadas,letra_atual):
        self.vidas=vidas
        self.letras_usadas=letras_usadas
        self.letra_atual=letra_atual

    def reset_vida(self):
        self.vidas=6
        return self.vidas
    def diminuir_vida(self):
        self.vidas=self.vidas-1
        return self.vidas
    def usar_letra(self):
        letra_atual=self.letra_atual
        letras_usadas=self.letras_usadas
        usada=False
        if letra_atual not in(letras_usadas):
            letras_usadas.append(letra_atual)
        else:
            usada=True
        return letras_usadas,usada

