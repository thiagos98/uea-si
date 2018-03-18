import random

matriz = [["","",""],["","",""],["","",""]]
linha = coluna = 0
terminou = False
def tabuleiro():
    print("%s | %s | %s        20 | 21 | 22"%(matriz[2][0],matriz[2][1],matriz[2][2]))
    print("---------")
    print("%s | %s | %s        10 | 11 | 12"%(matriz[1][0],matriz[1][1],matriz[1][2]))
    print("---------")
    print("%s | %s | %s        00 | 01 | 02"%(matriz[0][0],matriz[0][1],matriz[0][2]))

def leitura():
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    
def terminouVelha():
    terminou = False

    #jogos em linha
    for i in range(3):
        if (matriz[i][0] == matriz[i][1]) and (matriz[i][1] == matriz[i][2]):
            terminou = True
    #jogos em coluna
    for i in range(3):
        if (matriz[0][i] == matriz[1][i]) and (matriz[1][i] == matriz[2][i]):
            terminou = True
    #jogos em diagonal
    if (matriz[0][0] == matriz[1][1]) and (matriz[1][1] == matriz[2][2]):
        terminou = True
    elif (matriz[2][0] == matriz[1][1]) and (matriz[1][1] == matriz[0][2]):
        terminou = True

    #jogos em velha
    ocorr = 0
    for i in range(3):
        for j in range(3):
            if (matriz[i][j] != "X") and (matriz[i][j] != "O"):
                ocorr += 1

    if ocorr == 0:
        terminou = True

    return terminou    
#cont = 1
for i in range(3):
    for j in range(3):
        matriz[i][j] = " "
        
    
for i in range(9):
    if i % 2 == 0:
        tabuleiro()
        print("Informe a posicao da jogada.")
        leitura()
        if matriz[linha][coluna] == "X" or matriz[linha][coluna] == "O":
            print("Posicao invalida! Jogue novamente.")
            leitura()
            matriz[linha][coluna] = "X"
        else:
            matriz[linha][coluna] = "X"
        terminouVelha()
        if terminou == True:
            print("JOGO FINALIZADO!!!")
            break
    if i % 2 != 0:
        bot_linha = random.randrange(0,3)
        bot_coluna = random.randrange(0,3)
        while matriz[bot_linha][bot_coluna] == "X" or matriz[bot_linha][bot_coluna] == "O":
            bot_linha = random.randrange(0,3)
            bot_coluna = random.randrange(0,3)
        else:
            matriz[bot_linha][bot_coluna] = "O"
        terminouVelha()
        if terminou == True:
            print("JOGO FINALIZADO!!!")
            break

tabuleiro()
