#
#ipc_lista3.39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges - 1615310023
#Bruno de Oliveira Freire - 1615310030
#
N  = int(input("N:"))
cont = 1
H = 0
while cont < (N+1):
    print("1/",cont)
    H = H + (1/cont)
    cont = cont + 1
print("O resultado da serie ",H)
