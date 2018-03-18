numero1 = float(input("Digite um numero:"))
numero2 = float(input("Digite outro numero:"))

partedec1 = abs(numero1) - abs(int(numero1))
partedec2 = abs(numero2) - abs(int(numero2))

print("Qual operacao deseja realizar com esses numero?")
print("[1] Adicao")
print("[2] Subtracao")
print("[3] Multiplicacao")
print("[4] Divisao")

decisao = input("Resp->")

if decisao == "1":
    soma = numero1 + numero2
    if soma % 2 == 0:
        parimpar = "PAR"
    else:
        parimpar = "IMPAR"

    if soma >= 0:
        posneg = "POSITIVO"
    else:
        posneg = "NEGATIVO"

    if partedec1 + partedec2 != 0:
        numero = "DECIMAL"
    else:
        numero = "INTEIRO"

    print("Resultado:",soma)
    print("Número é ",parimpar,", ",posneg," e ",numero)
elif decisao == "2":
    subtracao = numero1 - numero2
    if subtracao % 2 == 0:
        parimpar = "PAR"
    else:
        parimpar = "IMPAR"

    if subtracao >= 0:
        posneg = "POSITIVO"
    else:
        posneg = "NEGATIVO"

    if partedec1 + partedec2 != 0:
        numero = "DECIMAL"
    else:
        numero = "INTEIRO"

    print("Resultado:",subtracao)
    print("Número é ",parimpar,", ",posneg," e ",numero)


elif decisao == "3":
    multiplicacao = numero1 * numero2
    if multiplicacao % 2 == 0:
        parimpar = "PAR"
    else:
        parimpar = "IMPAR"

    if multiplicacao >= 0:
        posneg = "POSITIVO"
    else:
        posneg = "NEGATIVO"

    if partedec1 + partedec2 != 0:
        numero = "DECIMAL"
    else:
        numero = "INTEIRO"

    print("Resultado:",multiplicacao)
    print("Número é ",parimpar,", ",posneg," e ",numero)
    
elif decisao == "4":
    divisao = numero1 / numero2
    if divisao % 2 == 0:
        parimpar = "PAR"
    else:
        parimpar = "IMPAR"

    if divisao >= 0:
        posneg = "POSITIVO"
    else:
        posneg = "NEGATIVO"

    if partedec1 + partedec2 != 0:
        numero = "DECIMAL"
    else:
        numero = "INTEIRO"

    print("Resultado:",divisao)
    print("Número é ",parimpar,", ",posneg," e ",numero)
