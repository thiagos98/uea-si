import math
print("Digite a seguir os coeficientes a, b e c para caucularmos as raizes da equacao.")

a = int(input("A:"))
if a == 0:
    print("Valor invalido")
else:
    b = int(input("B:"))
    c = int(input("C:"))

    delta = math.pow(b,2) - (4*a*c)
    if delta < 0:
        print("Delta negativo!Nao possui raizes reais.")
    elif delta == 0:
        print("Delta igual a zero!Possui uma raiz real.")
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        print("X1=",x1)
        print("X2=",x2)
    elif delta > 0:
        print("Delta positivo!Possui duas raizes reais distintas.")
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        print("X1=",x1)
        print("X2=",x2) 
