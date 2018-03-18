def cria_matriz (n_linha,n_coluna):
    for i in range(1,n_linha+1):
        linha = []
        for k in range(1,n_coluna+1):
            valor = int(input("Valor do elemento %d%d:"%(i,k)))
            linha.append(valor)
            print(linha)
        matriz.append(linha)

    return matriz

matriz = []

print("Linhas da matriz: ")
linha = int(input())
print("Colunas da matriz: ")
coluna = int(input())

matriz = cria_matriz(linha,coluna)

print("Matriz -> ",matriz)
