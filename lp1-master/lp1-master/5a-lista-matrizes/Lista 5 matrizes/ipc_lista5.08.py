#coding: utf-8
"""Imprimir as n primeiras linhas do triângulo de Pascal.
(b) Imprimir as n primeiras linhas do triângulo de Pascal usando apenas um vetor.
"""
#Thiago Santos Borges - 1615310023
#Antonio Rodrigues de Souza Neto - 1615310028
#Monitor: 

def calc_fatorial(numero):
	if numero == 1 or numero == 0:
		return 1
	else:
		return numero * calc_fatorial(numero - 1)

def analise_combinacional(numero,i):
	return calc_fatorial(numero)/(calc_fatorial(i) * calc_fatorial(numero - i))
	
def mostrar_matriz(matriz,linhas):
	print("Matriz")
	for i in range(linhas):
		print(matriz[i])
		

numero = int(input("Digite o numero de limite: "))
total = []
for numero in range(0,numero + 1):
	pascal = []
	for i in range(0,numero + 1):
		pascal.append(analise_combinacional(numero,i))
		total.append(pascal)
	print(pascal)
print(total)

