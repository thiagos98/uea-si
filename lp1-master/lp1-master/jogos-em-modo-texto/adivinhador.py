# adivinhador

import random

MAX_TENTATIVAS = 6

qtde_tentativas = 0

numero = random.randint(1,128)

print("Digite seu nome")
nome = input()

print("\nOla humano " + nome + ", adivinhe o numero entre 1 e 128 que eu estou pensando\n")
print("\nVocê tem no máximo 5 tentativas\n")

while qtde_tentativas < MAX_TENTATIVAS:
    print("Escolha um numero")
    tentativa = int(input())
    
    if tentativa > numero:
        print("alto demais!")
    
    if tentativa < numero:
        print("baixo demais!")
        
    if tentativa == numero:
        break
    
    qtde_tentativas = qtde_tentativas + 1
    print("Tentativa:" + str(qtde_tentativas) )
        
if tentativa == numero:
    print("Humano " + nome + ", você acertou. ! Humanidade salva")
    
if tentativa != numero:
    print("Humano " + nome + ", o numero era " + str(numero) )
    print("Humano " + nome + ", você falhou miseravelmente! Humanidade condenada")
        
