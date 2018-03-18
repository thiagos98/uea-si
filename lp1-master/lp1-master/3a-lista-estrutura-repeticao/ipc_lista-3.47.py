#
#ipc_lista3.39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges - 1615310023
#Bruno de Oliveira Freire - 1615310030
#
cont = 1
acmmedia = medianota = maior = menor = 0
cond = True
nome = input("Atleta: ")
while cont < 8:
    nota = float(input("Nota: "))
    if cont == 1:
        maior = menor = nota
    elif nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota
    acmmedia = (acmmedia + nota)
    cont = cont +1

acmmedia = acmmedia - maior - menor
cont = cont - 3
medianota = acmmedia / cont
print("Resultado final:\n")
print("Atleta: ",nome)
print("Melhor nota: %.1f" %maior)
print("Pior nota: %.1f" %menor)
print("Média: %.2f" %medianota)
cond = False
