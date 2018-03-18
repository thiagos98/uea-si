#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#

cont = 1
juros = 0
divida = float(input("Informe o valor da sua dívida->R$"))

print(' '*2+"Valor da Dívida"+' '*10+"Valor dos Juros"+' '*10+"Quant. de Parcelas"+' '*10+"Valor da Parcela")
while cont < 6:
    if i == 1:
        juros = 0
        parcelas = 1
    elif i == 2:
        juros = 0.1
        parcelas = 3
    elif i == 3:
        juros = 0.15
        parcelas = 6
    elif i == 4:
        juros = 0.2
        parcelas = 9
    elif i == 5:
        juros = 0.25
        parcelas = 12
        
    dividafinal = divida + (divida*juros)
    valorjuros = dividafinal - divida
    valorparcela = dividafinal / parcelas
    print(' '*2 + "R$", dividafinal ,' '*17 , "R$" , valorjuros , ' '*25 , parcelas, ' '*37 , "R$%.2f" % valorparcela)
    i = i + 1
