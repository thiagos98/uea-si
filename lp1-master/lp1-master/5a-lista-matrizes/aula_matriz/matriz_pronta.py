def crie (nlinha,ncoluna,valor):
    matriz = []
    for i in range(nlinha):
        linha = []
        for k in range(ncoluna):
            linha.append(valor)


        matriz.append(linha)
    return matriz

A = crie(5,5,0)
print(A)
