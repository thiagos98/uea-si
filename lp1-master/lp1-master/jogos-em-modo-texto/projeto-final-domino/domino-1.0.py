def pontos():
    for i in range(len(pontas)):
        soma = pontas[i] + soma
    
def verifica_jogada(jogada):
    verifica_jogada = False
    for i in range(len(peca)-1):
        while verifica_jogada == False:
            elemento = peca[i]
            if elemento == jogada:
                return capturar_jogada(jogada)  
            else:
                verifica_jogada = True
                print("Peca ja jogada")

def capturar_jogada(jogada):
    lado_1 = int(jogada[0]) 
    lado_2 = int(jogada[2])
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
peca = ['6,6','6,5','6,4','6,3','6,2','6,1','6,0',
        '5,5','5,4','5,3','5,2','5,1','5,0','4,4',
        '4,3','4,2','4,1','4,0','3,3','3,2','3,1',
        '3,0','2,2','2,1','2,0','1,1','1,0','0,0']

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
    verifica_jogada(jogada)
    peca_restante = mostrar_restante(peca, jogada,peca_restante)
    print("Pecas Restantes")    
    print(peca_restante)
    print(" ")
    print("As pontas sao:",pontas)
    print(" ")



