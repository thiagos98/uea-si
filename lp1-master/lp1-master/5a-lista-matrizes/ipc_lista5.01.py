"""1.  Dada uma matriz real A com m linhas e n colunas e um vetor real V com n elementos, determinar o produto de A por V. """

def criar_matriz(nlinhas,ncolunas):
    matriz = []
    linha = []
    for i in range(1,nlinhas+1):
        for j in range(1,ncolunas+1):
            valor = int(input("Elemento %d%d da matriz: "%(i,j)))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def criar_vetor(tam_vetor):
    vetor = []
    for i in range(1,tam_vetor+1):
        valor = int(input("Elemento %i do vetor: "%i))
        vetor.append(valor)
    return vetor

def multiplicar_vetor_matriz(matriz,vetor):
    matriz_multi = []
    quant_linha = len(matriz)
    quant_coluna = len(matriz[0])
    for i in range(quant_linha):
        valor = 0
        for j in range(quant_coluna):
            matriz_multi[i][j] += matriz[i][j] * vetor[j]

    return matriz_multi

linha = int(input("Numero de linhas: "))
colunavetor = int(input("Numero de colunas e tamanho do vetor: "))

multi = multiplicar_vetor_matriz(criar_matriz(linha,colunavetor),criar_vetor(colunavetor))
print(multi)
