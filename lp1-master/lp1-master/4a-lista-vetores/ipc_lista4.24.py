"""Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados."""
import random

LIMITE = 7
contdado = [0,0,0,0,0,0,0]
numero = []
for i in range(1,7):
    numero.append(i)
    
def aleatorio():
    return random.randrange(1,LIMITE)

for i in range(100):
    lance = aleatorio()
    if lance == 1:
        contdado[0] = contdado[0] + 1
    elif lance == 2:
        contdado[1] = contdado[1] + 1
    elif lance == 3:
        contdado[2] = contdado[2] + 1
    elif lance == 4:
        contdado[3] = contdado[3] + 1
    elif lance == 5:
        contdado[4] = contdado[4] + 1
    elif lance == 6:
        contdado[5] = contdado[5] + 1

for i,k in zip(numero,contdado):
    print("Numero %d foi contado %d vezes"%(i,k))
