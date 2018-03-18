lado1 = int(input("Lado 1:"))
lado2 = int(input("Lado 2:"))
lado3 = int(input("Lado 3:"))

if (lado1 < (lado2 + lado3)) and (lado2 < (lado1 + lado3)) and (lado3 < (lado1 + lado2)):
    escaleno = (lado1!=lado2) and (lado2!=lado3) and (lado1!=lado3)
    isosceles = (lado1==lado2) and (lado2 == lado3)
    equilatero = (lado1==lado2) and (lado3!=lado1) and (lado3!=lado2)
    print(lado1==lado2)
    print(lado2==lado3)
    print(equilatero)
    if escaleno == True:
        print("O trinagulo é escaleno.")
    elif isosceles == True:
        print("O triangulo é isosceles.")
    elif equilatero == True:
        print("O triangulo equilatero.")
else:
    print("Não pode formar um triangulo")
