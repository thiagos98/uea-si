#coding: utf-8
"""Dada uma matriz  Amxn, imprimir o numero de linhas e o 
número de colunas nulas da matriz."""
#Thiago Santos Borges - 1615310023
#Antonio Rodrigues de Souza Neto - 1615310028
#Monitor:
def criar_matriz(nlinha,ncoluna):
	matriz = []
	for i in range(1,nlinha + 1):
		linha = []
		for j in range(1,ncoluna + 1):
			elemento = int(input("M[%d][%d]: "%(i,j)))
			linha.append(elemento)
		matriz.append(linha)
	return matriz
	
def verificar_nulos(matriz,linha,coluna):
	cont_linha = 0
	cont_coluna = 0
	for i in range(linha):
		cont1 = 0
		cont2 = 0
		for j in range(coluna):
			if matriz[i][j] == 0:
				cont1 += 1
			if matriz[j][i] == 0:
				cont2 += 1
		if cont1 == linha or cont1 == coluna:
			cont_linha += 1
		if cont2 == linha or cont2 == coluna:
			cont_coluna += 1
	return cont_linha,cont_coluna
def mostrar_matriz(matriz,linhas):
	for i in range(linhas):
		print(matriz[i])

def main():
	linha = int(input("Linhas da matriz: "))
	coluna = int(input("Colunas da matriz: "))
	matriz = criar_matriz(linha,coluna)
	mostrar_matriz(matriz,linha)
	linha_nula, coluna_nula = verificar_nulos(matriz,linha,coluna)
	print("Numero de linhas nulas foi %d e %d de colunas nulas."%(linha_nula,coluna_nula))
	return 0
main()
