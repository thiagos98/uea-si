"""
(FEA 85) Deseja-se atualizar as contas correntes dos clientes de uma agência bancária. É dado o cadastro de n clientes contendo para cada cliente o número de sua conta e o seu saldo; o cadastro está ordenado pelo número da conta. Em seguida, é dado o número de operações efetuadas no dia e, para cada operação, o número da conta, uma letra C ou D indicando se a operação é de crédito ou débito e o valor da operação . Emitir o cadastro de clientes atualizado. 
"""
vetor=[]
auxiliar=[]

clientes=int(input("Digite quantos clientes são:"))
funcionario = []
for i in range(clientes):
    nome=input("Qual o seu nome ?:")
    auxiliar.append(nome)
    conta=int(input("Digite o número da conta corrente :"))
    auxiliar.append(conta)
    saldo=int(input("Digite o saldo da conta:"))
    auxiliar.append(saldo)
    funcionario.append(auxiliar)
    auxiliar=[]
    
for i in range(len(funcionario)):
    print("\n Nome:",funcionario[i][0])
    print("Número da conta:%d"%funcionario[i][1])
    print("Saldo total: R$%d"%funcionario[i][2])
 
operacoes=int(input("\n Digite quantas operações foram realizadas:"))
for a in range(operacoes):
    codigo=int(input("\n Digite o número da conta corrente ?"))
    if codigo==funcionario[i][1]:
        print("\n Seja bem vindo(a)",funcionario[i][0],"seu saldo é de R$:",funcionario[i][2] )
    
    funcao=str(input("Digite a operação que deseja (C)-C/crédito ou (D)-P/Débito:")).upper()
    
    if funcao=="C":
        quantia=float(input("Digite a quantia desejada para crédito:"))
        nova_quantia=funcionario[i][2]-quantia
    elif funcao=="D":
        quantia=float(input("Digite a quantia desejada para débito:"))
        nova_quantia=funcionario[i][2]-quantia
        
print("\n Dados após a atualização da conta")
print("Nome:",funcionario[i][0])
print("Saldo Total R$:",nova_quantia)

        
        
        

             