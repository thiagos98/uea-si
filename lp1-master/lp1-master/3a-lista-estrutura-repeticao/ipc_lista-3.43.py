#
#Usamos lista apenas para mostrar o menu :D
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#

nome = ["Cachorro Quente   ","Bauru simples        ","Bauru com ovo      ","Bamburguer           ","Cheeseburguer      ","Refrigerante           "]
codigo = [100,101,102,103,104,105]
preco = [1.2 , 1.3, 1.5, 1.2, 1.3, 1]
i = precofinal = precoaux = 0
cond = True

print("Especificação"+' '*10+"Código"+' '*3+"Preço")
while i < 6:
    print(nome[i],codigo[i]," "*5,"R$%.2f" %preco[i])
    i = i +1
while cond:
    cod = int(input("Digite o codigo do produto->"))
    quantidade = int(input("Digite a quantidade de produtos->"))
    if cod == codigo[0]:
        precoaux = preco[0] * quantidade
        print("Preço do produto->R$%.2f" %precoaux)
        precofinal = precofinal + precoaux
        print("Total do pedido até agora->R$%.2f" % precofinal)
    elif cod == codigo[1]:
        precoaux = preco[1] * quantidade
        print("Preço do produto->R$%.2f" %precoaux)
        precofinal = precofinal + precoaux
        print("Total do pedido até agora->R$%.2f" % precofinal)
    elif cod == codigo[2]:
        precoaux = preco[2] * quantidade
        print("Preço do produto->R$%.2f" %precoaux)
        precofinal = precofinal + precoaux
        print("Total do pedido até agora->R$%.2f" % precofinal)
    elif cod == codigo[3]:
        precoaux = preco[3] * quantidade
        print("Preço do produto->R$%.2f" %precoaux)
        precofinal = precofinal + precoaux
        print("Total do pedido até agora->R$%.2f" % precofinal)
    elif cod == codigo[4]:
        precoaux = preco[4] * quantidade
        print("Preço do produto->R$%.2f" %precoaux)
        precofinal = precofinal + precoaux
        print("Total do pedido até agora->R$%.2f" % precofinal)
    elif cod == codigo[5]:
        precoaux = preco[5] * quantidade
        print("Preço do produto->R$%.2f" %precoaux)
        precofinal = precofinal + precoaux
        print("Total do pedido até agora->R$%.2f" % precofinal)
    else:
        print("Digite um valor valido!")

    resp = input("Você quer continuar?? [s/n]")
    if resp == "s" or resp == "S":
        print("")
    elif resp == "n" or resp == "N":
        cond = False
        print("O preço final do seu pedido foi R$%.2f" %precofinal)
    else:
        print("Digite um valor valido!")
