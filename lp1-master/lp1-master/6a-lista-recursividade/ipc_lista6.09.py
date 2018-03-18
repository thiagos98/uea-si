#coding: utf-8
""" Crie uma função recursiva que receba um número inteiro positivo N e calcule o
somatório dos números de 1 a N"""

def somatorio(num):
    if num == 0:
        return 0
    else:
        return num + somatorio(num - 1)

print("Somatório do 1 ate N.\nInforme N: ")
num = int(input())
soma = somatorio(num)

print("Somatorio: ",soma)
