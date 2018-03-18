#coding: utf-8
"""Faça uma função recursiva que permita somar os elementos de um vetor de
inteiros"""

def somar(vetor,i):
    if i == len(vetor):
        return 0
    else:
        return vetor[i] + somar(vetor,i + 1)

def criar_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        valor = int(input("V[%d]: "%(i+1)))
        vetor.append(valor)
    return vetor

tamanho = int(input("tamanho: "))
vetor = criar_vetor(tamanho)
soma = somar(vetor,0)

print("A soma dos elementos do vetor é %d"%soma)

