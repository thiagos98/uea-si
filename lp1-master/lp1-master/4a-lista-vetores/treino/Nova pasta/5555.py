"""import random

LIMITE = 7
contdado = [0,0,0,0,0,0,0]
numero = []
for i in range(1,7):
    numero.append(i)
    
def aleatorio():
    return random.randrange(1,LIMITE)

for i in range(100):
    lance = aleatorio()
    if lance == 1:
        contdado[0] = contdado[0] + 1
    elif lance == 2:
        contdado[1] = contdado[1] + 1
    elif lance == 3:
        contdado[2] = contdado[2] + 1
    elif lance == 4:
        contdado[3] = contdado[3] + 1
    elif lance == 5:
        contdado[4] = contdado[4] + 1
    elif lance == 6:
        contdado[5] = contdado[5] + 1

for i,k in zip(numero,contdado):
    print("Numero %d foi lancado %d vezes"%(i,k))"""
"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
salto=["Primeiro Salto","Segundo Salto","Terceiro Salto","Quarto Salto","Quinto Salto"]
atleta=[]
saltos=[]
media=[]
soma=0
cond = True
while cond:
    nome=input("Digite o nome do atleta:")
    if nome == "":
        cond = False
    else:
        del saltos[0:5]
        atleta.append(nome)
        for i in range(5):
            salt=float(input("Digite o valor do %s:"%salto[i]))
            saltos.append(salt)
            soma=soma+saltos[i]
            media=soma/len(saltos)
        print("\n Resultado Final:")
        print("Atleta:",atleta)
        print("Saltos:",saltos)
        print("Média dos saltos:",media)
