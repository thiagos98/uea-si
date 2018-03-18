#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#
cond = True
acmjose = acmjoao = acmmaria = acmmario = acmnulo = acmbranco = acmtotal = porcentnulo = porcentbranco = 0
while cond:
    voto = int(input("1-Jose//2-Joao//3-Maria//4-Mario//5-Voto Nulo//6-Voto em Branco->"))
    if voto == 1:
        acmjose = acmjose + 1
        acmtotal = acmtotal + 1
    elif voto == 2:
        acmjoao = acmjoao + 1
        acmtotal = acmtotal + 1
    elif voto == 3:
        acmmaria = acmmaria + 1
        acmtotal = acmtotal + 1
    elif voto == 4:
        acmmario = acmmario + 1
        acmtotal = acmtotal + 1
    elif voto == 5:
        acmnulo = acmnulo + 1
        acmtotal = acmtotal + 1
    elif voto == 6:
        acmbranco = acmbranco + 1
        acmtotal = acmtotal + 1
    else:
        print("Digite um voto valido.")
        cond = False
    resp = input("Pessoas para votar? [s/n]")
    if resp == "s" or resp == "S":
        print("")
    elif resp == "n" or resp == "N":
        print("Votação encerrada.")
        cond = False
    else:
        print("Digite uma resposta valida.")
        
print("Votos Jose:",acmjose)
print("Votos Joao:",acmjoao)
print("Votos Maria:",acmmaria)
print("Votos Mario:",acmmario)
print("Votos Nulos:",acmnulo)
print("Votos em Branco:",acmbranco)

porcentnulo = (acmnulo / acmtotal)*100
porcentbranco = (acmbranco / acmtotal)*100

print("Porcentagem votos nulos:%.2f"%porcentnulo,"%")
print("Porcentagem votos em branco:%.2f"%porcentbranco,"%")
