turno = input("Em que turno voce estuda? [m-matutino/v-vespertino/n-noturno]\n")

if turno == "m":
    print("Bom dia!")
elif turno == "v":
    print("Boa tarde!")
elif turno == "n":
    print("Boa noite!")
else:
    print("Valor invalido!")
