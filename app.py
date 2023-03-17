# instancia as classes #responsavel: Hugo

import os
from mostrar_jogo import *
from computador import *
from jogador import *

def main():
    while True:
        Jogador1 = Jogador(6, '', '')
        palavra_original = "aviao"
        palavra_mostrar = ['_'] * Computador().tamanho_palavra()
        #PROBLEMA: TODA VEZ QUE A CLASSE COMPUTADOR É INSTANCIADA UMA NOVA PALAVRA É RANDOMIZADA

        while Jogador1.vidas > 0 and list(palavra_original) != palavra_mostrar:
        
            MostrarJogo.mostrar_cabecalho()
            MostrarJogo.mostrar_boneco(Jogador1.vidas)
            MostrarJogo.mostrar_vidas(Jogador1.vidas)
            MostrarJogo.mostrar_letras_usadas(Jogador1.letras_usadas)
            MostrarJogo.mostrar_palavra(palavra_mostrar)
            #MostrarJogo.mostrar_status(status_letra_usada, status_letra_correta, any, palavra_original, Jogador1.vidas) PROBLEMA: ROUNDS INTERMEDIÁRIOS TEM MENSAGEM DE DERROTA

            letra_palpite = input()
            setattr(Jogador1, 'letra_atual', letra_palpite)
            x, status_letra_usada = Jogador1.usar_letra()

            acertou = Computador().tentar_letra(letra_palpite, palavra_mostrar)
            if acertou:
                status_letra_correta = True
                #alguma maneira de trocar os underlines específicos pela letra_palpite na palavra_mostrar
            else:
                status_letra_correta = False
                Jogador1.diminuir_vida()

            limpar()

        if list(palavra_original) == palavra_mostrar:
            ganhou = True
        if Jogador1.vidas == 0:
            ganhou = False

        MostrarJogo.mostrar_cabecalho()
        MostrarJogo.mostrar_boneco(Jogador1.vidas)
        MostrarJogo.mostrar_vidas(Jogador1.vidas)
        MostrarJogo.mostrar_letras_usadas(Jogador1.letras_usadas)
        MostrarJogo.mostrar_palavra(palavra_mostrar)
        MostrarJogo.mostrar_status(False, False, ganhou, [palavra_original], Jogador1.vidas)


def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()
