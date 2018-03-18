vetor1 = []
vetor2 = []

for i in range(1,6):
    numero = int(input("Digite numero:"))
    vetor1.append(numero)

i = len(vetor1) - 1
while i >= 0:
    indice = vetor1[i]
    vetor2.append(indice)
    i = i - 1
print(vetor2)
