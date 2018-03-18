dia = int(input("Dia:"))
mes = int(input("Mes:"))
ano = int(input("Ano:"))
print(dia,"/",mes,"/",ano)

bissexto = True
if (ano % 400 == 0) or (ano % 4 ==0 and ano % 100 != 0):
    bissexto = True
else:
    bissexto = False

if dia > 0 and dia < 32:
    if mes > 0 and mes < 13:
        if mes == 2 and dia < 30 and bissexto:
            print("Data valida.")
        elif mes == 2 and dia > 30 and bissexto:
            print("Data invalida.")
        else:
            print("Data valida")
    else:
        print("Informe um mes valido.")
else:
    print("Informe um dia valido.")
    
