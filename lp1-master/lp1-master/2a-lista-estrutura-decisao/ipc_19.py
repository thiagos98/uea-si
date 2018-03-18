numero = input("Digite um numero menor que 1000 -> ")
qtnumero = len(str(numero))

if qtnumero == 3:
    centena = str(numero)[0:1]
    dezena = str(numero)[1:2]
    unidade = str(numero)[2:3]
    print(str(numero)+" = "+centena+" centenas, "+dezena+" dezenas e "+unidade+" unidades")
if qtnumero == 2:
    dezena = str(numero)[0:1]
    unidade = str(numero)[1:2]
    print(str(numero)+" = "+dezena+" dezenas e "+unidade+" unidades")
if qtnumero == 1:
    unidade = str(numero)[0:1]
    print(str(numero)+" = "+unidade+" unidades")
