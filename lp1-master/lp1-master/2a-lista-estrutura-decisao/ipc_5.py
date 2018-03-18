nota_1 = float(input("1a Nota Parcial:"))
nota_2 = float(input("2a Nota Parcial:"))

media = (nota_1 + nota_2)/2

if (media == 10):
    print("Aprovado com Distinção")
    print("Média:%.1f" %media)
elif (media >= 7):
    print("Aprovado")
    print("Média:%.1f" %media)
else:
    print("Reprovado")
    print("Média:%.1f" %media)
