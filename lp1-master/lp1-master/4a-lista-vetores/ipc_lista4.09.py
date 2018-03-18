a = []
soma = 0
quadrado = 1

for i in range(1,4):
    numero = int(input("Informe numero:"))
    a.append(numero)

for i in a:
    quadrado = i**2
    soma = soma + quadrado

print("A soma dos quadrados dos elementos e %d"%soma)
