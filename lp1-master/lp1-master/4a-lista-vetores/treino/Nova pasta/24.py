lista_lancamentos = []
lista_num_repeticoes = [0,0,0,0,0,0]
i = 1

for k in range(100):
    lista_lancamentos.append(i)
    if i == 6:
        i = i%6    
    i += 1
    
for k in range(100):
    if lista_lancamentos[k] == 1:
        lista_num_repeticoes[0] += 1
    elif lista_lancamentos[k] == 2:
        lista_num_repeticoes[1] += 1
    elif lista_lancamentos[k] == 3:
        lista_num_repeticoes[2] += 1
    elif lista_lancamentos[k] == 4:
        lista_num_repeticoes[3] += 1
    elif lista_lancamentos[k] == 5:
        lista_num_repeticoes[4] += 1
    else:
        lista_num_repeticoes[5] += 1
        i = i%6
    i += 1 
print(lista_lancamentos)
print(lista_num_repeticoes)
