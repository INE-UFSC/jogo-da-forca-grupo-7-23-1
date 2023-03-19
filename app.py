# instancia as classes #responsavel: Hugo

import os
from mostrar_jogo import *
from computador import *
from jogador import *
from gerador_palavras import escolhe_palavra

def main():
    while True:
        Jogador1 = Jogador(6, '', '')
        palavra_original = escolhe_palavra()
        palavra_mostrar = ['_'] * Computador(palavra_original).tamanho_palavra()
        status_letra_correta = False
        status_letra_usada = False

        while Jogador1.vidas > 0 and list(palavra_original) != palavra_mostrar:
        
            MostrarJogo.mostrar_cabecalho()
            MostrarJogo.mostrar_boneco(Jogador1.vidas)
            MostrarJogo.mostrar_vidas(Jogador1.vidas)
            MostrarJogo.mostrar_letras_usadas(Jogador1.letras_usadas)
            MostrarJogo.mostrar_palavra(palavra_mostrar)
            MostrarJogo.mostrar_status(status_letra_usada, status_letra_correta, 0, palavra_original, Jogador1.vidas) #PROBLEMA: ROUNDS INTERMEDIÁRIOS TEM MENSAGEM DE DERROTA

            letra_palpite = input('\n\n\033[0;33mInsira uma letra: ').lower()
            setattr(Jogador1, 'letra_atual', letra_palpite)
            x, status_letra_usada = Jogador1.usar_letra()

            acertou = Computador(palavra_original).tentar_letra(letra_palpite, palavra_mostrar)
            if acertou:
                status_letra_correta = True
            else:
                status_letra_correta = False
                Jogador1.diminuir_vida()

            limpar()

        if list(palavra_original) == palavra_mostrar:
            ganhou = 1
        if Jogador1.vidas == 0:
            ganhou = 2

        MostrarJogo.mostrar_cabecalho()
        MostrarJogo.mostrar_boneco(Jogador1.vidas)
        MostrarJogo.mostrar_vidas(Jogador1.vidas)
        MostrarJogo.mostrar_letras_usadas(Jogador1.letras_usadas)
        MostrarJogo.mostrar_palavra(palavra_mostrar)
        MostrarJogo.mostrar_status(False, False, ganhou, [palavra_original], Jogador1.vidas)
    
        continuar = str(input("\n\n\033[0;34mVocê deseja jogar novamente? [S/N] -> ")[0].lower())
        if continuar == 'n':
            break
    

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()
