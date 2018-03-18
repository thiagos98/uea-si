#coding: utf-8
"""Crie um programa em C, que contenha uma função recursiva que receba dois
inteiros positivos k e n e calcule kn
. Utilize apenas multiplicações. O programa principal
deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da
função"""

def pot(base,exp):
	if base == 0:
		return 0
	elif exp == 0:
		return 1
	elif exp == 1:
		return base
	elif exp > 1:
		return base * pot(base,exp - 1)

base = int(input("Base: "))
exp = int(input("Expoente: "))

potencia = pot(base,exp)                   
print(potencia)
