"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
"""

vetor = []
par = []
impar = []

for i in range(20):
    numero = int(input("Digite numero: "))
    vetor.append(numero)

for i in vetor:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print("Numeros: ",vetor)
print("Par: ",par)
print("Impar: ",impar)
