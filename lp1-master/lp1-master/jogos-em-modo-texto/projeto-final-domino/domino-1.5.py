def somar_pontas(pontas):
    soma = 0
    for i in range(len(pontas)):
        soma += pontas[i]
    if soma % 5 == 0:
        return soma
    else:
        return 0
def criar_pecas():
    pecas = []
    for i in range(6,0,-1):
        for j in range(6,0,-1):
            pecas.append((i,j))
    return pecas


def verifica_jogada(jogada,peca):
    verifica_jogada = False
    cont = 0
    for i in range(len(peca) - 1):
        if jogada == peca[i]:
            cont += 1

    while verifica_jogada == False:
        if cont == 1:
            return capturar_jogada(jogada)  
        else:
            verifica_jogada = True
            print("Peca ja jogada")

def capturar_jogada(jogada):
    lado_1 = int(jogada[0]) 
    lado_2 = int(jogada[1])
    return (atualiza_ponta(pontas,lado_1,lado_2))

def atualiza_ponta(pontas,lado_1,lado_2):
    ponta_1 = pontas[0]
    ponta_2 = pontas[1]
    ponta_3 = pontas[2]
    ponta_4 = pontas[3]
    lado_1 = lado_1
    lado_2 = lado_2
    if ponta_1 == lado_1:
        pontas[0] = lado_2
    elif ponta_2 == lado_1:
        pontas[1] = lado_2
    elif ponta_3 == lado_1:
        pontas[2] = lado_2
    elif ponta_4 == lado_1:
        pontas[3] = lado_2
    elif ponta_1 == lado_2:
        pontas[0] = lado_1
    elif ponta_2 == lado_2:
        pontas[1] = lado_1
    elif ponta_3 == lado_2:
        pontas[2] = lado_1
    elif ponta_4 == lado_2:
        pontas[3] = lado_1
    else:
        print("Peca invalida ou ja jogada")
    
    return (pontas)

def mostrar_restante(peca,jogada,peca_restante):
    for i in range(len(peca)-1):
        elemento = peca[i]
        if elemento == jogada:
            peca.pop(i)
            peca_restante = peca
    return peca_restante
     
#Variaveis Necessarias
peca = criar_pecas()

#Vetor de pecas jogadas
peca_jogada = []

#Vetor de pecas restantes
peca_restante =[]

#Pontas Iniciais
pontas = [6,6,6,6]

print("Pontas Iniciais", pontas)
print(" ")
while len(peca)>0:
    jogada = str(input("Digite a peca que deseja jogar: "))
    print(" ")
    ponta1,ponta2 = (int(jogada[0])),(int(jogada[2]))
    jogada = ponta1,ponta2
    verifica_jogada(jogada,peca)
    peca_restante = mostrar_restante(peca, jogada,peca_restante)
    soma = somar_pontas(pontas)
    print("Pecas Restantes")    
    print(peca_restante)
    print(" ")
    print("As pontas sao:",pontas)
    print(" ")
    print("A soma das pontas e:",soma)
    print(" ")
    