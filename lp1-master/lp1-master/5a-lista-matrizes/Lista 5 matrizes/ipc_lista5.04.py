"""Dada uma matriz real  Amxn, verificar se existem 
elementos repetidos em A"""
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

def verificar_repetidos(matriz,linha,coluna):
	k = 0
	l = 0
	repetido = False
	for i in range(linha):
		for j in range(coluna):
			k = i
			l = j + 1
			while not repetido and k < linha:
				while not repetido and l < coluna:
					if matriz[i][j] == matriz[k][l]:
						repetido = True
					l += 1
				l = 0
				k += 1
	return repetido
		
def mostrar_matriz(matriz,linhas):
	for i in range(linhas):
		print(matriz[i])

def main():
	linha = int(input("Linhas da matriz: "))
	coluna = int(input("Colunas da matriz: "))
	matriz = criar_matriz(linha,coluna)
	mostrar_matriz(matriz,linha)
	if verificar_repetidos(matriz,linha,coluna):
		print("Existe elementos repetidos")
	else:
		print("Nao existe elementos repetidos")
main()
