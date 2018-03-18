sal_hora = float(input("Quanto ganha por hora? R$"))
hora_mes = int(input("Trabalha quantas horas ao mês?"))

sal_bruto = sal_hora*hora_mes
imposto_renda = sal_bruto*11/100
inss = sal_bruto*(8/100)
sindicato=sal_bruto*(5/100)

print("+ Salário Bruto: R$",sal_bruto)
print("- IR(11%): R$",imposto_renda)
print("- INSS(8%): R$",inss)
print("- Sindicato(5%): R$",sindicato)
print("= Salário Líquido: R$",sal_bruto - (imposto_renda+inss+sindicato))
