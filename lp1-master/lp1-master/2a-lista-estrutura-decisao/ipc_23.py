
numero = float(input("Digite um numero:"))
partedec = abs(numero) - abs(int(numero))

if partedec != 0:
    print("Numero flutuante")
else:
    print("Numero inteiro")
