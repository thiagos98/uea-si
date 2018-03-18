def gerar_matriz(m, n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            valor = int(input("Matriz %d%d: "%(i, j)))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def gerar_vetor(n):
    vetor = []
    for i in range(n):
        valor = int(input("Vetor %d: "%i))
        vetor.append(valor)
    return vetor

def gerar_produto(matriz, vetor):
    linhas = len(matriz)
    colunas = len(matriz[0])
    produto = []
    for i in range(linhas):
        acm = 0
        for j in range(colunas):
            acm += matriz[i][j] * vetor1[j]
        produto.append(acm)
    return produto

def verificar(vetor, produto):
    if vetor == produto:
        print("Vetor Resultado")
    else:
        print("Nao e vetor resultado")

elementos = int(input("Elementos do vetor resultado: "))
vetor = gerar_vetor(elementos)
print(vetor)

print("Matriz A: ")
linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))
matriz = gerar_matriz(linhas, colunas)
for i in range(linhas):
    print(matriz[i])

print("Vetor X")
vetor1 = gerar_vetor(colunas)
print(vetor1)

print("Resultado")
resposta = gerar_produto(matriz, vetor)
print(resposta)
verificar(vetor, resposta)
