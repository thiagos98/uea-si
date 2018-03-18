#coding: utf-8
""" Faça uma função recursiva que receba um número inteiro positivo par N e
imprima todos os números pares de 0 até N em ordem crescente"""

def imprimir_par(numero):
    if numero == 0:
        return 0
    elif numero % 2 == 0:
        return str(imprimir_par(numero - 2))+" - "+str(numero)

numero = int(input("Digite um numero inteiro positivo par: "))
if numero % 2 == 0:
    numeros = imprimir_par(numero)
    print("Numeros pares de 0 ate %d: "%(numero),numeros)
else:
    print("Digitou numero invalido")
