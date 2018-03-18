PERCENTUAL_20 = 20/100
PERCENTUAL_15 = 15/100
PERCENTUAL_10 = 10/100
PERCENTUAL_5 = 5/100

salario = float(input("Informe seu salario para o reajuste: R$"))

if salario >= 0:
    
    if salario <= 280:

        salario_novo = salario + salario*PERCENTUAL_20
        percentual = PERCENTUAL_20
        valor_aumento = salario * PERCENTUAL_20
        
    elif salario > 280 and salario < 700:
        
        salario_novo = salario + salario*PERCENTUAL_15
        percentual = PERCENTUAL_15
        valor_aumento = salario * PERCENTUAL_15
        
    elif salario >= 700 and salario < 1500:
        
        salario_novo = salario + salario*0.1
        percentual = PERCENTUAL_10
        valor_aumento = salario * PERCENTUAL_10
        
    else:

        salario_novo = salario + salario*0.05
        percentual = PERCENTUAL_5
        valor_aumento = salario * PERCENTUAL_5

print("Salario anterior:R$",salario)
print("Percentual de aumento:",percentual)
print("Valor do aumento:R$",valor_aumento)
print("Valor do seu novo salario:R$",salario_novo)
