consoantes = []
letras = []
acm = 0
for i in range(1,11):
    letraind = input("Digite letra:")
    letras.append(letraind)
    if letraind == "a" or letraind == "e" or letraind == "i" or letraind == "o" or letraind == "u":
        acm = acm
    else:
        acm = acm + 1
        consoantes.append(letraind)

print("%d consoantes foram lidas.\nElas sao as seguintes %s"%(acm,consoantes))
