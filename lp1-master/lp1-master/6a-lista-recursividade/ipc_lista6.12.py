#coding: utf-8
""" Faça uma função recursiva que receba um
número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente"""

def mostrarcresc(numero,vet,aux):
    if aux > numero:
        return vet
    else:
        vet.append(aux)
        return mostrarcresc(numero,vet,aux + 1)

numero = int(input("Digite numero: "))
aux = 0
vet = []
impressao = mostrarcresc(numero,vet,aux)

print(impressao)
