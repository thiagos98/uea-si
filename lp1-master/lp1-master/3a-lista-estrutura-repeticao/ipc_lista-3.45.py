#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#

contador = 0
maior_nota = 0
menor_nota = 0
soma_notas = 0
condicao = True
while condicao:
    A = B = C = D = E = a = b = c = d = e = 1
    nota = 0
    questao = 1
    aluno = input("\nAluno: ")
    while questao <= 10:
        resposta = input("Resposta da questao %d: " % questao)
        if (questao == 1 and (resposta == "A" or resposta == "a")):
            nota = nota + 1
        if (questao == 2 and (resposta == "B" or resposta == "b")):
            nota = nota + 1
        if (questao == 3 and (resposta == "C" or resposta == "c")):
            nota = nota + 1
        if (questao == 4 and (resposta == "D" or resposta == "d")):
            nota = nota + 1
        if (questao == 5 and (resposta == "E" or resposta == "e")):
            nota = nota + 1
        if (questao == 6 and (resposta == "E" or resposta == "e")):
            nota = nota + 1
        if (questao == 7 and (resposta == "D" or resposta == "d")):
            nota = nota + 1
        if (questao == 8 and (resposta == "C" or resposta == "c")):
            nota = nota + 1
        if (questao == 9 and (resposta == "B" or resposta == "b")):
            nota = nota + 1
        if (questao == 10 and (resposta == "A" or resposta == "a")):
            nota = nota + 1
        questao +=1
    contador = contador + 1
    print("O aluno teve %d nota" % nota)
    soma_notas = soma_notas + nota
    if contador == 1:
        maior_nota = nota
        menor_nota = nota
    if contador > 1:
        if maior_nota < nota:
            maior_nota = nota
        elif maior_nota > nota:
            maior_nota = maior_nota
    if contador > 1:
        if menor_nota < nota:
            menor_nota = menor_nota
        elif menor_nota > nota:
            menor_nota = nota
    uso = 0
    while uso == 0:
        uso = str(input("\nInformar outro aluno? S-SIM/N-NAO \n"))
        if uso == "s" or uso == "S":
            condicao = True
        elif uso == "n" or uso == "N":
            condicao = False
        else:
            print("Valor invalido!")
            uso = 0
media_turma = (soma_notas)/(contador)

print ("Maior acerto: ",maior_nota)
print ("Menor acerto: ",menor_nota)
print ("%d alunos usaram o programa." % contador)
print ("Média da turma: ",media_turma)
