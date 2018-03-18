ap1 = float(input("Digite a nota AP1:"))
ap2 = float(input("Digite a nota AP2:"))

media = (ap1 + ap2)/2

if media >= 9 and media <= 10:
    aproveitamento = "A"
    situacao = "APROVADO"
elif media >= 7.5 and media < 9:
    aproveitamento = "B"
    situacao = "APROVADO"
elif media >= 6 and media < 7.5:
    aproveitamento = "C"
    situacao = "APROVADO"
elif media >= 4 and media < 6:
    aproveitamento = "D"
    situacao = "REPROVADO"
elif media >= 0 and media < 4:
    aproveitamento = "E"
    situacao = "REPROVADO"
else:
    print("Valor informado de AP1 ou AP2 invalidos!")

print("\nAP1:%.1f" %ap1)
print("AP2:%.1f" %ap2)
print("Média:%.1f" %media)
print("Conceito de aproveitamento:",aproveitamento)
print("Situação:",situacao)
