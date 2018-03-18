

cond = True

nomes = ["1- necessita da esfera","2- necessita de limpeza","3- necessita troca do cabo ou conector","4- quebrado ou inutilizado"]
quant_defeito = [0,0,0,0]
porcento = [0,0,0,0]
soma = 0
simbolo = "%"

print("=======DEFEITOS=======")
for i in nomes:
    print(i)

while cond:
    numero = int(input("Numero do defeito(0=sair): "))
    if numero == 0:
        cond = False
    elif numero > 4 or numero < 0:
        print("Digite um defeito valido!")
    else:
        if numero == 1:
            quant_defeito[0] += 1
            soma += 1
        elif numero == 2:
            quant_defeito[1] += 1
            soma += 1
        elif numero == 3:
            quant_defeito[2] += 1
            soma += 1
        elif numero == 4:
            quant_defeito[3] += 1
            soma += 1

for i,k in zip(quant_defeito,range(0,4)):
    porcento[k] = porcento[k] + ((i * 100)/soma)

print("Situacao                        Quantidade            Percentual")
print("1- necessita de esfera                  %d                   %.1f%s"%(quant_defeito[0],porcento[0],simbolo))
print("2- necessita de limpeza                 %d                   %.1f%s"%(quant_defeito[1],porcento[1],simbolo))
print("3- necessita troca do cabo ou conector  %d                   %.1f%s"%(quant_defeito[2],porcento[2],simbolo))
print("4- quebrado ou inutilizado              %d                   %.1f%s"%(quant_defeito[3],porcento[3],simbolo))

