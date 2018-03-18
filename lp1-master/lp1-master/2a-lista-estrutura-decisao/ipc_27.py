
morangos = float(input("Quilos de morango->"))
macas = float(input("Quilos de maçãs->"))
totalquilos = morangos + macas

if morangos <= 5:
    pmorango = 2.5
else:
    pmorango = 2.2

if macas <= 5:
    pmaca = 1.8
else:
    pmaca = 1.5

fmorango = pmorango * morangos
fmaca = pmaca * macas
pfinal = fmorango + fmaca

if totalquilos > 8 or pfinal > 25:
    pfinal = pfinal - (pfinal*0.1)
    print("O preço a ser pago é R$%.2f" %pfinal)
else:
    print("O preço a ser pago é R$%.2f" %pfinal)

 
