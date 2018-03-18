notas = []
media = acm = 0

for i in range(1,5):
    notaind = float(input("Informe a nota:"))
    notas.append(notaind)
    acm = acm + notaind

media = acm / i
for i in notas:
    print("Notas:%.1f"%i)
print("A media e %.1f"%media)
