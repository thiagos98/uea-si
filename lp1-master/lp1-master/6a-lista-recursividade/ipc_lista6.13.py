#coding: utf-8
"""Faça uma função recursiva que receba um número
inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente"""

def mostrardec(numero,vet):
    if numero < 0:
        return vet
    else:
        vet.append(numero)
        return mostrardec(numero - 1,vet)

numero = int(input("Digite numero: "))
vet = []
impressao = mostrardec(numero,vet)

print(impressao)
