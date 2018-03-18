#coding: utf-8
"""Um vetor real X com n elementos é apresentado como resultado de um sistema de equações lineares Ax = B cujos coeficientes 
são representados em uma matriz real Amxn e os lados direitos das equações em um vetor real B de m elementos. 
Verificar se o vetor X é realmente solução do sistema dado."""
#Thiago Santos Borges - 1615310023
#Antonio Rodrigues de Souza Neto - 1615310028
#Monitor: Lucas Botinelly
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
	for i in range(1,tamanho + 1):
		valor = int(input("V[%d]: "%(i)))
		vetor.append(valor)
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

def verificar_resultado(solucao,resultado):
	if solucao == resultado:
		return True
	else:
		return False
def mostrar_matriz(matriz,linhas):
	for i in range(linhas):
		print(matriz[i])


tamanho_solucao = int(input("tamanho vetor Teste: "))
solucao = criar_vetor(tamanho_solucao)

linha = int(input("Quantas linhas tem a matriz de coeficiente? "))
coluna = int(input("Quantas colunas tem a matriz de coeficiente? "))
matriz = criar_matriz(linha,coluna)

print("Vetor X")
tamanho_X = coluna
vetor = criar_vetor(tamanho_X)

resultado = multiplicar_vetor(matriz,vetor)
print("\nMatriz")
mostrar_matriz(matriz,linha)
if verificar_resultado(solucao,resultado):
	print("Resultado Correto")
else:
	print("Resultado incorreto")
