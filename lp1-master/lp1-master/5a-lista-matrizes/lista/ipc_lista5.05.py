"""Dizemos que uma matriz inteira Anxn  e uma matriz de permutacao se em 
cada linha e em cada coluna houver n-1 elementos nulos e 
um unico elemento igual a 1"""
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

def verificar_permutacao(matriz,linha,coluna):
	for i in range(linha):
		acm_linha = 0
		acm_coluna = 0
		for j in range(coluna):
			if matriz[i][j] == 1 or matriz[i][j] == 0:
				if matriz[i][j] == 1:
					acm_linha += 1
				if matriz[j][i] == 1:
					acm_coluna += 1
			else:
				return False
				
	if acm_linha == 1 and acm_coluna == 1:
		return True
	else:
		return False
		
def mostrar_matriz(matriz,linhas):
	for i in range(linhas):
		print(matriz[i])

def main():
	linha = int(input("Linhas da matriz: "))
	coluna = int(input("Colunas da matriz: "))
	if linha != coluna:
		print("Linha deve ser igual a coluna!")
	else:
		matriz = criar_matriz(linha,coluna)
		mostrar_matriz(matriz,linha)
		if verificar_permutacao(matriz,linha,coluna):
			print("E matriz permutacao")
		else:
			print("Nao e matriz permutacao")
main()
