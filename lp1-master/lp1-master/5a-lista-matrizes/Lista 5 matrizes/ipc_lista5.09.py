"""Dada uma matriz real A com m linhas e n colunas e um vetor 
real V com n elementos, determinar o produto de A por V"""
#Thiago Santos Borges - 1615310023
#Antonio Rodrigues de Souza Neto - 1615310028
#Monitor: 
def criar_matriz(nlinha,ncoluna):
	matriz = []
	for i in range(1,nlinha + 1):
		linha = []
		for j in range(1,ncoluna + 1):
			elemento = 0
			linha.append(elemento)
		matriz.append(linha)
	return matriz

def mostrar_matriz(matriz,linhas):
	print("Matriz")
	for i in range(linhas):
		print(matriz[i])
		
linha = int(input("Digite quantidade de linhas: "))
coluna = int(input("Digite quantidade de colunas: "))
matriz = criar_matriz(linha,coluna)
for i in range(1,linha):
	matriz[i][0] += -1
	matriz[i][coluna] += -1
for j in range(coluna + 1):
	matriz[0][j] += -1
	matriz[linha][j] += -1
print(matriz)
