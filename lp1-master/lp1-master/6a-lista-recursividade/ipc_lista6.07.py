#coding: utf-8
#Thiago Santos Borges - 1615310023
#Antonio Rodrigues de Souza Neto - 1615310028
""" Crie um programa em C que receba um vetor de números reais com 100 elementos.
Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor"""

def criarvetor(tamanho):
    vetor = []
    for i in range(tamanho):
        valor = int(input("V[%d]: "%(i + 1)))
        vetor.append(valor)
    return vetor

def inverter(vetor,i,inverso):
    if i == -1:
        return inverso
    else:
        inverso.append(vetor[i])
        return inverter(vetor,i - 1,inverso)

tamanho = int(input("Inversão dos valores do vetor\nTamanho do vetor: "))
vetor = criarvetor(tamanho)
inverso = []
vetinverso = inverter(vetor,(len(vetor) - 1),inverso)
print(vetinverso)
