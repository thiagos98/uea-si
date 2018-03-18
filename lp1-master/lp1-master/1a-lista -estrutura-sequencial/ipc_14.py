peso=float(input("Peso dos peixes->"))
limite=50.0
if (peso > limite):
    print("A excesso de peixes!")
    excesso=peso-limite
    multa=excesso*4
    print("O(s) kilos excedentes foram ",excesso)
    print("Multa->R$",multa)
else:
    print("Multa->R$",0)
