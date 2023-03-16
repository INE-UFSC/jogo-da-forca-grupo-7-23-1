#mostra as acoes na tela # responsavel: Constante
class MostrarJogo:
    def mostrar_cabecalho():
        return print(120*"\033[1;37m-"), print("\033[1;37m|", 50*" ","\033[1;37mJOGO DA FORCA",51*" " ,"|"), print(120*"\033[1;37m-")


    def mostrar_boneco(vidas_atual = 6):
        if vidas_atual == 6:
            print("\033[0;31m+---+   ")
            print("\033[0;31m|   |   ")
            print("\033[0;31m|       ")
            print("\033[0;31m|       ")
            print("\033[0;31m|       ")
            print("\033[0;31m|       ")
        
        elif vidas_atual == 5:
            print("\033[0;31m+---+   ")
            print("\033[0;31m|   |   ")
            print("\033[0;31m|   O   ")
            print("\033[0;31m|       ")
            print("\033[0;31m|       ")
            print("\033[0;31m|       ")
        
        elif vidas_atual == 4:
            print("\033[0;31m+---+   ")
            print("\033[0;31m|   |   ")
            print("\033[0;31m|   O   ")
            print("\033[0;31m|   |   ")
            print("\033[0;31m|       ")
            print("\033[0;31m|       ")
        
        elif vidas_atual == 3:
            print("\033[0;31m+---+   ")
            print("\033[0;31m|   |   ")
            print("\033[0;31m|   O   ")
            print("\033[0;31m|   |\  ")
            print("\033[0;31m|       ")
            print("\033[0;31m|       ")
        
        elif vidas_atual == 2:
            print("\033[0;31m+---+   ")
            print("\033[0;31m|   |   ")
            print("\033[0;31m|   O   ")
            print("\033[0;31m|  /|\  ")
            print("\033[0;31m|       ")
            print("\033[0;31m|       ")
            
        elif vidas_atual == 1:
            print("\033[0;31m+---+   ")
            print("\033[0;31m|   |   ")
            print("\033[0;31m|   O   ")
            print("\033[0;31m|  /|\  ")
            print("\033[0;31m|    \  ")
            print("\033[0;31m|       ")
            
        elif vidas_atual == 0:
            print("\033[0;31m+---+   ")
            print("\033[0;31m|   |   ")
            print("\033[0;31m|   O   ")
            print("\033[0;31m|  /|\  ")
            print("\033[0;31m|  / \  ")
            print("\033[0;31m|       ")


    def mostrar_vidas(vidas_atual = 6):
        return print(f"\n\033[1;37mContexto: Palavras Aleatórias | \033[0;34mTentativas restantes: {vidas_atual}\n")


    def mostrar_letras_usadas(letras_usadas = []):
        print("\033[1;33mLetras sugeridas: ", end = " ")
        for a, letra in enumerate(letras_usadas): print(f"{letra.upper()} - ", end = " ")
    
    
    def mostrar_palavra(palavra_atual = []):
        print("\n\n\033[0;33mPalavra atualizada: ", end = " ")
        for b, palavra in enumerate(palavra_atual): print(f" {palavra}\n")


    def mostrar_status(status_letras_usadas = False, status_letras_corretas = False, ganhou = False, palavra_secreta = ["teste"], vidas_atual = 6):
        if status_letras_usadas == True:
            print("\n\033[0;31mEsta letra já foi sugerida. Tente novamente.")
        
        if status_letras_corretas == True:
            print("\n\033[0;32mParabéns, esta letra existe na palavra secreta.")
            
        if ganhou == True:
            print("\n\033[0;32mParabéns!!! Você venceu!!!\n")
        else:
            print(f"\n\033[0;31mQue pena, você perdeu!!! A palavra secreta era: {palavra_secreta[0]}\n")