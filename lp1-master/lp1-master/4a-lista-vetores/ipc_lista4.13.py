mes = ["Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
tempmes = []
acm = 0
QUANT_MES = 12
medianual = 0

for i in range(12):
    temp = float(input("Temperatura media do mes de %s:"%mes[i]))
    tempmes.append(temp)
    acm = acm + temp

medianual = acm / QUANT_MES

print("Media anual:%d"%medianual)
for i in range(12):
    if tempmes[i] > medianual:
        print("%d - %s: %.1f"%(i+1,mes[i],tempmes[i])) 
