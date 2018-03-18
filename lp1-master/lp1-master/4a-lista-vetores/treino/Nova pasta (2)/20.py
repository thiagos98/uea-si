
abonovet = []
salvet = []

SAL_MINIMO = 500
ABONO_MIN = 100
TAXA = 0.2

total_func = 0
valor_gasto = 0
valor_maior = 0
total_minimo = 0

cond = True

print("Projeção de Gastos com Abono\n============================")
while cond:
    salario = float(input("Digite salario: R$"))
    if salario == 0:
        cond = False
    elif salario <= 500:
        salvet.append(salario)
        abonovet.append(ABONO_MIN)
        total_func = total_func + 1
        total_minimo = total_minimo + 1
        valor_gasto = valor_gasto + ABONO_MIN
    else:
        abono = salario * TAXA
        salvet.append(salario)
        abonovet.append(abono)
        total_func = total_func + 1
        valor_gasto = valor_gasto + abono
        if abono > valor_maior:
            valor_maior = abono

print("Salário     - Abono")
for i,k in zip(salvet,abonovet):
    print("R$ %8.2f - R$ %5.2f"%(i,k))

print("Foram processados %d colaboradores."%total_func)
print("Total gasto com abonos: R$%8.2f."%valor_gasto)
print("Valor minimo pago a %d colaboradores."%total_minimo)
print("Maior valor de abono pago. R$%5.2f"%valor_maior)
