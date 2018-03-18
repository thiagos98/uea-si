MEDIA = 7
MEDIA_10 = 10
nota1 = float(input("Nota 1->"))
nota2 = float(input("Nota 2->"))
nota3 = float(input("Nota 3->"))

media = (nota1 + nota2 + nota3)/3

if media == MEDIA_10:
    print("Aprovado com Distinção!")
    print("Média->%.2f" %media)
elif media >= MEDIA:
    print("Aprovado!")
    print("Média->%.2f" %media)
else:
    print("Reprovado!")
    print("Média->%.2f" %media)
