"""Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um vetores ou lista ou array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante"""


cond = True
acm = 200
TAXA = 0.09
venda = 0
salario = []
contvalor = [0,0,0,0,0,0,0,0,0]
numero = []

for i in range(1,10):
    numero.append(i)

while cond:
    venda = int(input("Informe sua venda semanal(-1=sair): $"))
    if venda == -1:
        cond = False
    else:
        salario.append((venda*TAXA + acm))


for i in salario:
    if i >= 200 and i < 300:
        contvalor[0] = contvalor[0]+1    
    elif i >= 300 and i < 400:
        contvalor[1] = contvalor[1]+1
    elif i >= 400 and i < 500:
        contvalor[2] = contvalor[2]+1
    elif i >= 500 and i < 600:
        contvalor[3] = contvalor[3]+1
    elif i >= 600 and i < 700:
        contvalor[4] = contvalor[4]+1
    elif i >= 700 and i < 800:
        contvalor[5] = contvalor[5]+1
    elif i >= 800 and i < 900:
        contvalor[6] = contvalor[6]+1
    elif i >= 900 and i < 1000:
        contvalor[7] = contvalor[7]+1
    elif i >= 1000:
        contvalor[8] = contvalor[8]+1


for i,k in zip(contvalor,numero):
    print(k,"-",i)

