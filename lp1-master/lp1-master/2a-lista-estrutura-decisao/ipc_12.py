IR_0 = 0
IR_5 = 0.05
IR_10 = 0.10
IR_20 = 0.20
SINDICATO = 0.03
INSS = 0.10
FGTS = 0.11

salario_hora = float(input("Quantos reais por hora? R$"))
horas_mes = int(input("Horas trabalhadas ao mes:"))

salario_bruto = salario_hora * horas_mes
print(salario_bruto)
if salario_bruto <= 900:
    
    salario_liquido = salario_bruto - salario_bruto * IR_0
    salario_liquido = salario_bruto - salario_bruto * SINDICATO
    salario_liquido = salario_bruto - salario_bruto * INSS
    fgts = salario_bruto * FGTS
    ir = IR_0
    
elif salario_bruto > 900 and salario_bruto <= 1500:
    
    salario_liquido = salario_bruto - salario_bruto * IR_5
    salario_liquido = salario_bruto - salario_bruto * SINDICATO
    salario_liquido = salario_bruto - salario_bruto * INSS
    fgts = salario_bruto * FGTS
    ir = IR_5
    
elif salario_bruto > 1500 and salario_bruto <= 2500:

    salario_liquido = salario_bruto - salario_bruto * IR_10
    salario_liquido = salario_bruto - salario_bruto * SINDICATO
    salario_liquido = salario_bruto - salario_bruto * INSS
    fgts = salario_bruto * FGTS
    ir = IR_10
else:

    salario_liquido = salario_bruto - salario_bruto * IR_20
    salario_liquido = salario_bruto - salario_bruto * SINDICATO
    salario_liquido = salario_bruto - salario_bruto * INSS
    fgts = salario_bruto * FGTS
    ir = IR_20
    
print("\nSalario Bruto        : R$",salario_bruto)
print("(-) IR               : R$",salario_bruto * ir)
print("(-) INSS             : R$",salario_bruto * INSS)
print("(-) SINDICATO        : R$",salario_bruto * SINDICATO)
print("FGTS(",FGTS,")         : R$",salario_bruto * FGTS)
print("Total de descontos   : R$",(salario_bruto * ir)+(salario_bruto * INSS) + (salario_bruto * SINDICATO))
print("Salario Liquido      : R$",salario_bruto - ((salario_bruto * ir)+(salario_bruto * INSS) + (salario_bruto * SINDICATO)))
