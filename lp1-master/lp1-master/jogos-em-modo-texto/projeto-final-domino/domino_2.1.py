def criar_pecas(ponta_min,ponta_max):
    pecas = []
    for i in range(ponta_max,ponta_min,-1):
        for j in range(ponta_max,ponta_min,-1):
            if i>=j:
                pecas.append((i,j))
    return pecas

def verifica_jogada(jogada,peca_restante, pontas):
    for i in range(len(peca_restante)):
        if jogada == peca_restante[i]:
            for i in range(len(pontas)):
                if jogada[0] == pontas[i]:
                    return True
                elif jogada[1] == pontas[i]:
                    return True
        else:
            return False               

def captura_peca():
    jogada = str(input("Digite a peca que deseja jogar: "))
    print(" ")
    return (jogada)

def atualiza_ponta(jogada,pontas):
    print("ponta 0 = lado esquerdo  ponta 1 = cima")
    print("ponta 2 = lado direito   ponta 3 = baixo")
    print(" --Pontas--")
    print(" 0, 1, 2, 3")
    print(pontas)
    ponta = int(input("Qual ponta quer jogar? "))
    for i in range(len(pontas)):
        if i == ponta:
            if jogada[0] == jogada[1]:
                pontas[i] = jogada[0] + "*"
            else:
                if pontas[i] == jogada[0]:
                    pontas[i] = jogada[1]
                    verifica = True
                elif pontas[i] == jogada[1]:
                    pontas[i] = jogada[0]
                    verifica = True
                else:
                    print("\n Ponta diferente da peca")
                    verifica = False
    return pontas,ponta,verifica

def atualiza_pecas_restante(jogada,peca_restante):
    for i in range(len(peca_restante)-1):
        elemento = peca_restante[i]
        if elemento == jogada:
            peca_restante.pop(i)
            peca_restante = peca
    return (peca_restante)

def pontuacao(pontas,pontos,ponta,contador):
    if contador == 1:
        return pontuacao_1(pontas,ponta)
    elif contador == 2 or contador == 3:
        return pontuacao_2_3(pontas,ponta)
    else:
        return pontuacao_resto(pontas)
def pontuacao_1(pontas,ponta):
    pontos = 12 + pontas[ponta]
    if pontos % 5 == 0:
        return pontos
    else: return 0
def pontuacao_2_3(pontas,ponta):
    pontos = 0
    for i in range(len(pontas)):
        if pontas[i] != 6:
            pontos += pontas[i]
    if pontos % 5 == 0:
        return pontos
    else: return 0
def pontuacao_resto(pontas):
    pontos = 0
    for i in range(len(pontas)):
        pontos += pontas[i]
    if pontos % 5 == 0:    
        return pontos
    else: return 0
    
#minimo e maximo de ponta
ponta_min = -1
ponta_max = 6
#Variaveis Necessarias
peca = criar_pecas(ponta_min,ponta_max)
peca.pop(0)
peca = peca 
#Vetor de pecas jogadas
peca_jogada = []
#Vetor de pecas restantes
peca_restante = peca
#Pontas Iniciais
pontas = [6,6,6,6]
#Pontos
pontos = 0
#contador das rodadas
contador = 1

print("Pontas Iniciais", pontas, "\n")
while len(peca)>0:
    print("Exemplo: 6,5 \n")
    jogada = captura_peca()                                      #Captura peca jogada
    ponta1,ponta2 = (int(jogada[0])),(int(jogada[2]))            #Separa a string em pontas
    jogada = ponta1,ponta2                                       #transforma pontas em peca
    verifica = verifica_jogada(jogada,peca_restante,pontas)      #Verifica Jogada Valida
    
    if verifica == True:                                         #Se Jogada Valida Atualiza pontas e pontos
        pontas,ponta,verifica = atualiza_ponta(jogada,pontas)
        if verifica == True:
            peca_restante = atualiza_pecas_restante(jogada, peca_restante)
            pontos = pontuacao(pontas,pontos,ponta,contador)
        contador += 1
    print("\n Pecas Restantes \n",peca_restante)    
    print("\n As pontas sao:",pontas)
    print("\n Pontos: ", pontos)
    print(" ")