"""Dadas duas matrizes reais  Amxn e Bnxp, calcular o produto de A por B"""
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
	
def multiplicar_matriz(matriz1,matriz2):
	produto = []
	linha1 = len(matriz1)
	linha2 = len(matriz2)
	coluna2 = len(matriz2[0])
	for i in range(linha1):
		linha = []
		for j in range(coluna2):
			acm = 0
			for k in range(linha2):
				acm += matriz1[i][k] * matriz2[k][j]
			linha.append(acm)
		produto.append(linha)
	return produto
	
def mostrar_matriz(matriz,linhas):
	for i in range(linhas):
		print(matriz[i])

def main():
	linha1 = int(input("Linhas matriz 1: "))
	coluna1 = int(input("Colunas matriz 1: "))
	linha2 = int(input("Linhas matriz 2: "))
	if coluna1 != linha2:
		print("Nao existe produto!")
	else:
		coluna2 = int(input("Colunas matriz 2: "))
		print("Matriz 1")
		matriz1 = criar_matriz(linha1,coluna1)
		print("Matriz 2")
		matriz2 = criar_matriz(linha2,coluna2)
		print("Matriz 1")
		mostrar_matriz(matriz1,linha1)
		print("Matriz 2")
		mostrar_matriz(matriz2,linha2)
		produto = multiplicar_matriz(matriz1,matriz2)
		print("Matriz 1 * Matriz 2 -> ",produto)
main()
