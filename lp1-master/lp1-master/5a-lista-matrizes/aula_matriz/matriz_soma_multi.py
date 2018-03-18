#luizaugustomm -> GitHub

def somar(m1, m2):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

def mult_escalar(matriz, escalar):
    matriz_mult = []
    quant_linhas = len(matriz) # Conta quantas linhas existem
    quant_colunas = len(matriz[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_mult
        matriz_mult.append([])
        for j in range(quant_colunas):
            # Multiplicando cada elemento pelo escalar
            mult = escalar * matriz[i][j]
            matriz_mult[i].append(mult)
    return matriz_mult

escalar = 10
matriz1 = [[1,5],[2,6]]
matriz2 = [[4,5],[3,4]]
mult = mult_escalar(matriz1,escalar)
mult = mult_escalar(matriz2,escalar)
soma = somar(matriz1,matriz2)


print("Matriz 1 -> ",matriz1)
print("Matriz 2 -> ",matriz2)
print("Matriz 1 * 10 -> ",mult)
print("Matriz 2 * 10 -> ",mult)
print("Matriz 1 + Matriz 2 -> ",soma)
