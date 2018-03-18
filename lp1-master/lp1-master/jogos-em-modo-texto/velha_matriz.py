import random

matriz = [["","",""],["","",""],["","",""]]

def tabuleiro():
    print("%s | %s | %s"%(matriz[2][0],matriz[2][1],matriz[2][2]))
    print("---------")
    print("%s | %s | %s"%(matriz[1][0],matriz[1][1],matriz[1][2]))
    print("---------")
    print("%s | %s | %s"%(matriz[0][0],matriz[0][1],matriz[0][2]))

def mudarjogador(simbol):
    if simbol == "X":
        simbol = "O"
    else:
        simbol = "X"

def jogar(simbolo,posicao):
    mudou = False
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == str(posicao):
                matriz[i][j] = simbolo
                mudou = True

    return mudou

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
    
#main
cont = 1
simb = "X"
R = True
for i in range(3):
    for j in range(3):
        matriz[i][j] = cont
        cont += 1
tabuleiro()

while (terminouVelha() == False):
    while(R == True):
        print("Vai jogar em qual posicao?")
        pos = str(input())
        R = jogar(simb,pos)
        if R == True:
            print("Jogada invalida")
    mudarjogador(simb)
    tabuleiro()
print("JOGO FINALIZADO!!!")

    
