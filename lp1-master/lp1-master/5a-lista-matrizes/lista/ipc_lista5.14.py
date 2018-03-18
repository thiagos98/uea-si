def calcular_custo(matriz):
    soma = 0
    vetor_int = []
    paradas = int(input("Quantas paradas estao programadas?\n"))
    for i in range(paradas):
        intinerario = int(input("Qual intinerario a ser percorrido?[limite 0 - %d]: "%(linha-1)))
        vetor_int.append(intinerario)
    tamanho = len(vetor_int)
    for i in range(paradas):
        if i != (tamanho - 1):
            m = vetor_int[i]
            n = vetor_int[i+1]
            soma += matriz[m][n]
    return soma
def criar_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input("VALOR[%d][%d]: R$"%(i,j)))
            linha.append(valor)
        matriz.append(linha)
    print("Tabela Montada!")
    for i in range(linhas):
        print(matriz[i])
    return matriz



print("Calculadora de custos de transporte.")
custos = int(input("O tamanho da tabela de custos: "))
linha = coluna = custos
tabela = criar_matriz(linha,coluna)

custo = calcular_custo(tabela)
print("\nO custo da viajem foi R$%d"%custo)
