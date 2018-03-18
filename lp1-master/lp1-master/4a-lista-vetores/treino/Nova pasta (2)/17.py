
sequencia = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
saltos = []

cond = True
soma = 0
media = 0

while cond:
    nome = str(input("\nAtleta: "))
    if nome == "":
        cond = False
    else:
        media = 0
        soma = 0
        del saltos[0:5]
        for i in sequencia:
            distancia = float(input("%s Salto: "%i))
            saltos.append(distancia)
            soma = soma + distancia
        media = soma / len(saltos)
        print("\nResultado Final: ")
        print("Atleta: %s"%nome)
        print("Saltos:",saltos)
        print("Media dos saltos: %.1f m"%media)
