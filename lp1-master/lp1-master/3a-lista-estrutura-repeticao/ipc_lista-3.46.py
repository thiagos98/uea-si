#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#
maior = menor = acmmedia = 0
cont = 1
SALTOS = 6
nome = input("Atleta: ")

while cont < SALTOS:
    print(cont,"° Salto:")
    nota = float(input(""))
    if cont == 1:
        maior = menor = nota
    elif nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota
    acmmedia = acmmedia + nota
    cont = cont + 1

acmmedia = acmmedia - (maior + menor)
mediafinal = acmmedia / (cont - 3)
print("\nMelhor salto: %.1f" %maior)
print("Pior salto: %.1f" %menor)
print("Média dos demais saltos: %.1f" %mediafinal)
print("\nResultado final:")
print(nome+": %.2f"%mediafinal)
