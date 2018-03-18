#coding: utf-8
""" Faça uma função recursiva que receba um
número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente"""

def pardec(numero,vet):
    if numero < 0:
        return vet
    else:
        vet.append(numero)
        return pardec(numero - 2,vet)

numero = int(input("Digite numero par: "))
if numero % 2 != 0:
    print("Deveria ter digitado um numero par!!!")
else:
    vet = []
    par = pardec(numero,vet)
    print(par)    
