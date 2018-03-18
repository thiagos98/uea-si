par = []
impar = []
numeros = []

for i in range(1,11):
    numero = int(input("Digite numero:"))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Numeros digitados->",numeros)
print("Numero digitados pares->",par)
print("Numero digitados impares->",impar)
