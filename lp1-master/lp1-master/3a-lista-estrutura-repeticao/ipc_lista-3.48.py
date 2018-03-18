#
#ipc_lista3.39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges - 1615310023
#Bruno de Oliveira Freire - 1615310030
#
numero = int(input("Digite um numero:"))
aux = numero
reverso = 0

while aux != 0:
    reverso = reverso * 10 + aux % 10
    aux = aux // 10

print("O reverso de numero %d \ne %d"%(numero,reverso))

