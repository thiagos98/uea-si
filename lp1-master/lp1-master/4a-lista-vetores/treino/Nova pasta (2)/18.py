lista_votos = []
lista_jogador = []
lista_votos_cada = []
lista_porcentagem = []
cont1 = 0
cont2 = 1
fim = 1
cond = True
v = 23
por_cento ="%"

for i in range(v):
    i += 1
    lista_jogador.append(i)
    lista_votos_cada.append(cont1)
    lista_porcentagem.append(cont1)

print("Qual foi o jogador mais importante da partida?")

while cond:
    num = int(input("Informe o numero da camisa do jogador(informe 0 para parar o programa):\n"))
    if num >= 1 and num < v:
        cont1 += 1
        for i in range(v):
            if lista_jogador[i] == num:
                lista_votos_cada[i] += 1
    elif num > 23:
        print("numero invalido, vote nas camisas entre 1 a 23")
    elif num == 0:
        cond = False

for i in range(v):
    if lista_votos_cada[i] != 0:
        porcentagem = (lista_votos_cada[i]*100)/(cont1)
        lista_porcentagem[i] = porcentagem
        
maior = lista_votos_cada[0]
maior_num = 0

for i in range(v):    
    if maior < lista_votos_cada[i]:
        maior = lista_votos_cada[i]
        maior_num = i + 1
        porcentagem_maior = lista_porcentagem[i]
        
print("Resultado da votação:")
print("Foram computados %d voto(s) no total"%cont1)
print("Jogador    |     voto(s)     | porcentagem(%)")
for i in range(v):
    if lista_votos_cada[i] != 0:
        print("%s          |     %s           |    %s%s"%(lista_jogador[i],lista_votos_cada[i],lista_porcentagem[i],por_cento))
print("O melhor jogador foi o de camisa %s,com %s voto(s), correspondendo a %s%s dos votos totais"%(maior_num,maior,porcentagem_maior,por_cento))

