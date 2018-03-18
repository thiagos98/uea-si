"""Dadas duas matrizes reais  Amxn e Bnxp, calcular o produto de A por B"""
from matriz import*

print("Digite o tamanho da matriz A")
linhasA = int(input("Linhas: "))
colunaA = int(input("Colunas: "))
print("Matriz A")
matrizA = criar_matriz(linhasA,colunaA)
print("Digite o tamanho da matriz B")
linhaB = int(input("Linhas: "))
colunaB = int(input("Colunas: "))
if colunaA != linhaB:
    print("Nao existe produto da matriz A por B")
else:
    print("Matriz B")
    matrizB = criar_matriz(linhaB,colunaB)
    matrizC = multiplicar_matrizes(matrizA,matrizB)
    print("Matriz A * Matriz B -> ",matrizC)
