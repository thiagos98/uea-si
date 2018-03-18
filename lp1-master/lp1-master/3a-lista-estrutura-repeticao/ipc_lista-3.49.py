#
#ipc_lista3.39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges - 1615310023
#Bruno de Oliveira Freire - 1615310030
#
cont = 0
n = 1
m = 1
soma = 0
limite = int(input("Digite limite:"))
while cont < limite:
    print(n,"/",m)
    soma = soma + (n/m)
    n = n + 1
    m = m +2
    cont = cont + 1
    
print("A soma da serie ",soma)
