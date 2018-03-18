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
	    elemento = int(input("M[%d][%d]: "%(i,j)))
	    linha.append(elemento)
	matriz.append(linha)
    return matriz
	
def criar_vetor(tamanho):
    vetor = []
    for j in range(1,tamanho + 1):
	elemento = int(input("V[%d]: "%j))
	vetor.append(elemento)
    return vetor

def multiplicar_vetor(matriz,vetor):
    linha = len(matriz)
    coluna = len(matriz[0])
    produto = []
    for i in range(linha):
	acm = 0
	for j in range(coluna):
	    acm += matriz[i][j] * vetor[j]
	produto.append(acm)
    return produto
	
def mostrar_matriz(matriz,linhas):
    print("Matriz")
    for i in range(linhas):
	print(matriz[i])

def main():
    linha = int(input("Digite quantidade de linhas: "))
    coluna = int(input("Digite quantidade de colunas: "))
    tamanho = int(input("Digite tamanho do vetor: "))
    if coluna != tamanho:
	print("Nao existe produto!")
    else:
	matriz = criar_matriz(linha,coluna)
	vetor = criar_vetor(tamanho)
	produto = multiplicar_vetor(matriz,vetor)
	mostrar_matriz(matriz,linha)
	print("Vetor: \n",vetor)
	print("Matriz * Vetor -> ",produto)
main()
