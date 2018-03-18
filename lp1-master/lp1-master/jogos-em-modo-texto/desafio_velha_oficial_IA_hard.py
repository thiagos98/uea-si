#Introdução a programação de computadores
#Professor: Jucimar Junior
#Thiago Santos Borges - 1615310023
#Bruno de Oliveira Freire - 1615310030
#Nickso Patrick Façanha Calheiros - 1615310059
#Mateus Mota de Souza - 1615310016
#Igor Menezes Sales Vieira - 1615310007
#Nadine da Cunha Brito - 1615310040
#Ana Jessye Almeida Antunes - 1615310046
import random


vetor = ["1","2","3","4","5","6","7","8","9"]
cont = 0

while cont < 9:
    
    if cont % 2 == 0:
        print("###Jogo da Velha###")
        print("%s | %s | %s" %(vetor[6],vetor[7],vetor[8]))
        print("---------")
        print("%s | %s | %s" %(vetor[3],vetor[4],vetor[5]))
        print("---------")
        print("%s | %s | %s" %(vetor[0],vetor[1],vetor[2]))
        jogada = int(input("Digite um valor de 1~9:\n"))
        jogada -= 1
        if vetor[jogada] == "X" or vetor[jogada] == "O":
            print("Posicao invalida! Jogue novamente")
            jogada = int(input())
            jogada -= 1
            vetor[jogada] = "X"
        else:
            vetor[jogada] = "X"
        if vetor[0] == vetor[1] and vetor[1] == vetor[2] or vetor[3] == vetor[4] and vetor[4] == vetor[5] or vetor[6] == vetor[7] and vetor[7] == vetor[8] or vetor[0] == vetor[3] and vetor[3] == vetor[6] or vetor[1] == vetor[4] and vetor[4] == vetor[7] or vetor[2] == vetor[5] and vetor[5] == vetor[8] or vetor[0] == vetor[4] and vetor[4] == vetor[8] or vetor[2] == vetor[4] and vetor[4] == vetor[6]:
            print("Parabens!!! Voce venceu uma burrice artificial!!!\m/")
            cont = 10
"""
1. Ganhar: Se você tem duas peças numa linha, ponha a terceira.
2. Bloquear: Se o oponente tiver duas peças em linha, ponha a terceira para bloqueá-lo.
3. Triângulo: Crie uma oportunidade em que você poderá ganhar de duas maneiras.
4. Bloquear o Triângulo do oponente:
    Opção 1: Crie 2 peças em linha para forçar o oponente a se defender, contanto que não resulte nele criando um triângulo ou vencendo.
             Por exemplo, se 'X' tem dois cantos opostos do tabuleiro e 'O' tem o centro, 'O' não pode jogar num canto
             (Jogar no canto nesse cenário criaria um triângulo em que 'X' vence).
    Opção 2: Se existe uma configuração em que o oponente pode formar um triângulo, bloqueiem-no.
5. Centro: Jogue no centro.
6. Canto vazio: jogue num canto vazio."""

if cont % 2 != 0:
        """bot = random.randrange(0,9)
        while vetor[bot] == "X" or vetor[bot] == "O":
            bot = random.randrange(0,9)
        else:
            vetor[bot] = "O"
        if vetor[0] == vetor[1] and vetor[1] == vetor[2] or vetor[3] == vetor[4] and vetor[4] == vetor[5] or vetor[6] == vetor[7] and vetor[7] == vetor[8] or vetor[0] == vetor[3] and vetor[3] == vetor[6] or vetor[1] == vetor[4] and vetor[4] == vetor[7] or vetor[2] == vetor[5] and vetor[5] == vetor[8] or vetor[0] == vetor[4] and vetor[4] == vetor[8] or vetor[2] == vetor[4] and vetor[4] == vetor[6]:
            print("Voce perdeu miseravelmente para uma maquina burra!!!")
            cont = 10"""

        for i in vetor:
            if vetor[0] and vetor[3] == "O":
                vetor[6] = "O"
            elif vetor[0] and vetor[6] == "O":
                vetor[3] = "O"
            elif vetor[3] and vetor[6] == "O":
                vetor[6] = "O"
    cont += 1
if cont == 9:
    print("Jogo Velhou!!!")
    
print("###Jogo da Velha###")
print("%s | %s | %s" %(vetor[6],vetor[7],vetor[8]))
print("---------")
print("%s | %s | %s" %(vetor[3],vetor[4],vetor[5]))
print("---------")
print("%s | %s | %s" %(vetor[0],vetor[1],vetor[2]))
