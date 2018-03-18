#coding: utf-8
"""Dizemos que uma matriz quadrada inteira é um quadrado mágico (1) se a soma dos elementos de cada linha, 
a soma dos elementos de cada coluna e a soma dos 
elementos das diagonais principal e secundária são todas iguais.
Dada uma matriz quadrada Anxn , verificar se A é um quadrado mágico"""
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
	
def diagonal_principal(matriz):
	linha = len(matriz)
	coluna = len(matriz[0])
	principal = []
	for i in range(linha):
		acm = 0
		for j in range(coluna):
			if i == j:
				acm += matriz[i][j]
		principal.append(acm)
	return principal

def diagonal_secundaria(matriz):
	linha = len(matriz)
	coluna = len(matriz[0])
	secundaria = []
	for i in range(linha):
		acm = 0
		for j in range(coluna):
			if (i + j) == (linha - 1):
				acm += matriz[i][j]
		secundaria.append(acm)
	return secundaria

def linhas(matriz):
	linha = len(matriz)
	coluna = len(matriz[0])
	linhas = []
	for i in range(linha):
		acm = 0
		for j in range(coluna):
			acm += matriz[i][j]
		linhas.append(acm)
	return linhas

def colunas(matriz):
	linha = len(matriz)
	coluna = len(matriz[0])
	colunas = []
	for i in range(linha):
		acm = 0
		for j in range(coluna):
			acm += matriz[j][i]
		colunas.append(acm)
	return colunas
	
def testar_cubo(soma):
	
	cont = 0
	for i in soma:
		if i == soma[0]:
			cont += 1
	if cont == len(soma):
		return True
	else:
		return False

def mostrar_matriz(matriz,linhas):
	for i in range(linhas):
		print(matriz[i])

def main():
	linha = int(input("Linhas da matriz: "))
	coluna = int(input("Colunas da matriz: "))
	matriz = criar_matriz(linha,coluna)
	if linha != coluna:
		print("Linhas devem ser igual a colunas")
	else:
		mostrar_matriz(matriz,linha)
		principal = diagonal_principal(matriz)
		secundaria = diagonal_secundaria(matriz)
		varlinha = linhas(matriz)
		varcoluna = colunas(matriz)
		principal.extend(secundaria)
		principal.extend(varlinha)
		principal.extend(varcoluna)
		if testar_cubo(principal):
			print("E cubo")
		else:
			print("Nao e cubo")
main()
