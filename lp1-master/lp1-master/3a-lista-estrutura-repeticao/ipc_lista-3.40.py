#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#

cont = 1
ind_maior = ind_menor = codigo_maior = codigo_menor = num_veiculos = num_acidente = num_macidente = 0
while (cont < 3):
    codigocid = int(input("Informe o codigo da cidade:"))
    veiculopasseio = int(input("Informe o numero de veiculos de passeio na determinada cidade:"))
    acidentetransito = int(input("Informe o numero de acidentes com vitimas:"))
    
    if (cont == 1):
        ind_maior = ind_menor = acidentetransito
        codigo_maior = codigo_menor = codigocid
    elif acidentetransito >= ind_maior:
        ind_maior = acidentetransito
        codigo_maior = codigocid
    elif acidentetransito <= ind_menor:
        ind_menor = acidentetransito
        codigo_menor = codigocid

    if veiculopasseio < 2000:
        num_acidente = num_acidente + acidentetransito
        num_macidente = num_macidente + 1
    num_veiculos = num_veiculos + veiculopasseio

    cont = cont + 1
mediaveic = num_veiculos / cont-1
mediacidente = num_acidente / num_macidente

print(num_acidente)
print(num_macidente)
print("\nN° maior indice de acidentes->",ind_maior,".Codigo da cidade->",codigo_maior)
print("N° menor indice de acidentes->",ind_menor,".Codigo da cidade->",codigo_menor)
print("Media de veiculos:",mediaveic)
print("Media de acidentes de transito em cidades com menos de 2000 veiculos:",mediacidente)
