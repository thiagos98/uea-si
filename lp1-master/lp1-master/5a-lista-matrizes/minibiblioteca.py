def criar_matriz(n_linhas,n_colunas):
    matriz = []
    for i in range(1,n_linhas + 1):
        linha = []
        for j in range(1,n_colunas + 1):
            valor = float(input("Elemento %i%i: "%(i,j)))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def multiplicar_matrizes(matrizA,matrizB):
    matrizC = []
    linhasA = len(matrizA)
    colunasA = len(matrizA[0])
    linhasB = len(matrizB)
    colunasB = len(matrizB[0])
    
    for i in range(linhasA):
        linhac = []
        for j in range(colunasB):
            acm = 0
            for k in range(linhasB):   
                acm += matrizA[i][k] * matrizB[k][j]
            linhac.append(valor)
        matrizC.append(linhac)
    return matrizC

def multiplicar_matriz_vetor(matriz,vetor,linhas,colunas):
    produto = []
    for i in range(linhas):
        acm = 0
        for j in range(colunas):
            acm += matriz[i][j] * vetor[j]
        produto.append(acm)
    return produto

def criar_vetor(tam_vetor):
    vetor = []
    for i in range(1,tam_vetor+1):
        valor = int(input("Elemento %i do vetor: "%i))
        vetor.append(valor)
    return vetor
