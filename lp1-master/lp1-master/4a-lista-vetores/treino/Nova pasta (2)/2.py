"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
vetor = []
vetorinv = []

for i in range(10):
    numero = float(input("Digite numero: "))
    vetor.append(numero)

i = len(vetor) - 1
while i >= 0:
    vetorinv.append(vetor[i])
    i = i - 1

print("Vetor: ",vetor)
print("Inverso: ",vetorinv)
