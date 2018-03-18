peca = []
#Variaveis Necessarias
for i in range(6,0,-1):
    for j in range(6,0,-1):
        peca.append((i,j))
print(peca)

#Vetor de pecas jogadas
peca_jogada = []

#Vetor de pecas restantes
peca_restante =[]

#Pontas Iniciais
pontas = [6,6,6,6]

print("Pontas Iniciais", pontas)
print(" ")
for i in range(36):
    print(peca[i])