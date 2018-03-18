#coding: utf-8
"""O hiperfatorial de um número N, escrito H(n), é definido por  (N^N)*(N-1)^(N-1)
Faça uma função recursiva que receba um número inteiro positivo N e retorne o hiperfatorial desse número."""

def hiperfat(num):
    if num == 1:
        return 1
    else:
        return num ** num * hiperfat(num - 1)
    
numero = int(input("Calcular o Hiperfatorial\nDigite o numero: "))
hiper = hiperfat(numero)
print(hiper)
