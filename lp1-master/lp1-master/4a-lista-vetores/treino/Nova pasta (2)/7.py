"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

vetor = []
multi = 1
soma = 0

for i in range(5):
    numero = int(input("Digite numero: "))
    vetor.append(numero)
    multi *= numero
    soma += numero

print(vetor)
print(multi)
print(soma)
