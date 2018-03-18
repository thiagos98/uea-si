acmacima = 0
acm7 = 0
acm = 0
soma = 0
media = 0
nota = 0
notas = []
notasinv = []

while nota != -1:
    nota = float(input("Informe sua nota: "))
    if nota == -1:
        acm = acm
        soma = soma
    else:
        notas.append(nota)
        acm = acm + 1
        soma = soma + nota
    
media = soma / acm

for i in notas:
    if i > media:
        acmacima = acmacima + 1
    elif i < 7:
        acm7 = acm7 + 1
        
for i in notas[::-1]:
    notasinv.append(i)
    
print("Foram lidos %d notas"%acm)
print("Notas:",notas)
print("Notas na ordem inversa:")
for i in notasinv:
    print(i)

print("A soma das notas:%d"%soma)
print("A media das notas:%.1f"%media)
print("Quantidade de notas acima da media:%d"%acmacima)
print("Quantidade de notas abaixo de 7:%d"%acm7)
