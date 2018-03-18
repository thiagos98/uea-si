saltos = []
sequencia = ["Primeiro","Segundo","Terceiro","Quarto","Quinta"]
media = 0
acm = 0

nome = raw_input("Atleta: ")
print("")
for k in range(5):
    salto = float(input("%s Salto:"%sequencia[k]))
    saltos.append(salto)
    acm = acm + salto

media = acm / 5
print("Resultado Final:\nAtleta: $s\nSaltos: %d - \nMedia dos saltos: %.1f m"%(nome,salto,media))
