#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#
cond = True
cont25 = cont50 = cont75 = cont100 = 0
while cond:
    numero = int(input("Digite um numero:"))
    if numero < 0:
        print("Numero invalido")
        cond = False
    elif numero >= 0 and numero <= 25:
        cont25 = cont25 + 1
    elif numero >= 26 and numero <= 50:
        cont50 = cont50 + 1
    elif numero >= 51 and numero <= 75:
        cont75 = cont75 + 1
    elif numero >= 76 and numero <= 100:
        cont100 = cont100 + 1

print("[0]-[25]:",cont25,"//[26]-[50]:",cont50,"//[51]-[75]:",cont75,"//[76]-[100]:",cont100)
