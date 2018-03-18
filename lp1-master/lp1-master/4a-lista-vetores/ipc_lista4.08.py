idade = []
altura = []
idadeinv = []
alturainv = []

for i in range(1,4):
    id_pessoa = int(input("Informe sua idade->"))
    alt_pessoa = float(input("Inform sua altura(m)->"))
    idade.append(id_pessoa)
    altura.append(alt_pessoa)

i = len(idade) - 1
while i >= 0: 
    idadeinv.append(idade[i])
    i = i - 1

i = len(altura) - 1
while i >= 0:
    alturainv.append(altura[i])
    i = i - 1

print(idade)    
print(idadeinv)
print("\n",altura)
print(alturainv)
