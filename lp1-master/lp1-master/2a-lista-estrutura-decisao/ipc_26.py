ALCOOL = 1.9
GASOLINA = 2.5

litros = float(input("Litros:"))
tipo = input("A-álcool/G-gasolina:")

if tipo == "A" or tipo == "a":
    if litros <= 20:
        preco = litros * ALCOOL
        print(preco)
        precofinal = preco -  litros * (preco *( 3/100))
    elif litros > 20:
        preco = litros * ALCOOL
        precofinal = preco - (litros - 20) * (preco *( 3/100))
elif tipo == "G" or tipo == "g":
    if litros <= 20:
        preco = litros * GASOLINA
        precofinal = preco - (litros) * (preco *( 4/100))
    elif litros > 20:
        preco = litros * GASOLINA
        precofinal = preco - (litros - 20) * (preco *( 6/100))
else:
    print("Digite um tipo valido de combustivel.")

print("Valor final:R$ %.2f" %abs(precofinal))
