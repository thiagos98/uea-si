#Thiago Santos Borges - 1615310023
#Antonio Rodrigues de Souza Neto - 1615310028
def cadastrar_clientes():
    auxiliar=[]
    clientes=int(input("Digite quantos clientes o banco possui -> "))
    funcionario = []
    for i in range(clientes):
        nome=input("Qual o seu nome?\n")
        auxiliar.append(nome)
        conta=int(input("Digite o número da conta corrente -> \n"))
        auxiliar.append(conta)
        saldo=int(input("Saldo da sua conta -> \nR$"))
        auxiliar.append(saldo)
        funcionario.append(auxiliar)
        auxiliar=[]

    return funcionario

def mostrar_dados_provisorios(funcionario):    
    for i in range(len(funcionario)):
        print("Nome:%s"%funcionario[i][0])
        print("Número da conta:%d"%funcionario[i][1])
        print("Saldo total: R$%d"%funcionario[i][2])

def mostrar_dados_permanentes(funcionario):
    print("Nome - Nº conta - Saldo Atual")
    for i in range(len(funcionario)):
        print(funcionario[i])

def alterar_banco_de_dados(funcionario):
    n_operacoes = int(input("Digite quantas operações devem ser realizadas ->"))
    for k in range(n_operacoes):
        novo_saldo = 0
        n_conta = int(input("Digite o número da conta -> "))
        for i in range(len(funcionario)):
            if n_conta == funcionario[i][1]:
                operacao = str(input("Qual tipo de operacao deseja realizar.[d-debito/c-credito] ->"))
                if operacao == "C" or operacao == "c":
                    quantia = float(input("Digite a quantia desejada para crédito ->R$"))
                    funcionario[i][2] -= quantia
                elif operacao == "D" or operacao == "d":
                    quantia = float(input("Digite a quantia desejada para débito ->R$"))
                    funcionario[i][2] -= quantia
                print("Dados atualizados da sua conta\n")
                print("Nome:",funcionario[i][0])
                print("Saldo Total R$:",funcionario[i][2])

    return funcionario
funcionario = cadastrar_clientes()
mostrar_dados_provisorios(funcionario)
funcionario = alterar_banco_de_dados(funcionario)
mostrar_dados_permanentes(funcionario)
