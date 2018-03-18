#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#
cont = 1
maior = menor = num_maior = num_menor = 0
while (cont < 4):
    num = int(input("Digite a matricula do aluno:"))
    altura = float(input("Digite a altura(cm):"))
    if (cont == 1):
        num_maior = num_menor = num
        maior = menor = altura
    elif altura >= maior:
        maior = altura
        num_maior = num
    elif altura <= menor:
        menor = altura
        num_menor = num
    i = i + 1
print("\nMatricula do maior aluno->%d"%num_maior,". Altura(cm)->", maior)
print("Matricula do menor aluno->%d" %num_menor,". Altura(cm)->", menor)
    
