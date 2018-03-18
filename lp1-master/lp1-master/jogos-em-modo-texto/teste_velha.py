#encoder UTF-8
import random

tabuleiro = """
===Jogo da Velha===
===Tabela de numeros para jogada===
 7 | 8 | 9
-----------
 4 | 5 | 6
-----------
 1 | 2 | 3
\n
"""
vetor = ["1","2","3","4","5","6","7","8","9"]
print(tabuleiro)

cont = 0
while cont < 9:
    """print("\n%s | %s | %s" %(vetor[6],vetor[7],vetor[8]))
    print("----------")
    print("%s | %s | %s" %(vetor[3],vetor[4],vetor[5]))
    print("----------")
    print("%s | %s | %s" %(vetor[0],vetor[1],vetor[2]))
"""
    if cont % 2 == 0:
        print("\n%s | %s | %s" %(vetor[6],vetor[7],vetor[8]))
        print("----------")
        print("%s | %s | %s" %(vetor[3],vetor[4],vetor[5]))
        print("----------")
        print("%s | %s | %s" %(vetor[0],vetor[1],vetor[2]))
        print("Escolha um numero de 1-9")
        jogada = int(input())
        if vetor[(jogada - 1)] == "X" or vetor[(jogada - 1)] == "O":
            print("Lugar ja esta ocupado!Jogue novamente em um local valido.")
            jogada = int(input())
            vetor[jogada - 1] = "X"
        else:
            vetor[(jogada - 1)] = "X"
        if vetor[0] == vetor[1] and vetor[1] == vetor[2] or vetor[3] == vetor[4] and vetor[4] == vetor[5] or vetor[6] == vetor[7] and vetor[7] == vetor[8] or vetor[0] == vetor[3] and vetor[3] == vetor[6] or vetor[1] == vetor[4] and vetor[4] == vetor[7] or vetor[2] == vetor[5] and vetor[5] == vetor[8] or vetor[0] == vetor[4] and vetor[4] == vetor[8] or vetor[2] == vetor[4] and vetor[4] == vetor[6]:
            print ("Voce ganhou, voce e o bixao mesrmo em doido !!!")
            print("\n%s | %s | %s" %(vetor[6],vetor[7],vetor[8]))
            print("----------")
            print("%s | %s | %s" %(vetor[3],vetor[4],vetor[5]))
            print("----------")
            print("%s | %s | %s" %(vetor[0],vetor[1],vetor[2]))
            cont = 20
    if cont % 2 != 0:
        bot = random.randint(0,8)
        while vetor[bot] == "X" or vetor[bot] == "O":
            bot = random.randint(0,8)
        else:
            vetor[bot] = "O"
            
        if vetor[0] == vetor[1] and vetor[1] == vetor[2] or vetor[3] == vetor[4] and vetor[4] == vetor[5] or vetor[6] == vetor[7] and vetor[7] == vetor[8] or vetor[0] == vetor[3] and vetor[3] == vetor[6] or vetor[1] == vetor[4] and vetor[4] == vetor[7] or vetor[2] == vetor[5] and vetor[5] == vetor[8] or vetor[0] == vetor[4] and vetor[4] == vetor[8] or vetor[2] == vetor[4] and vetor[4] == vetor[6]:
            print ("Voce perdeu para a maquina mais burra do mundo, voce e o bixao mesrmo em doido !!!")
            print("\n%s | %s | %s" %(vetor[6],vetor[7],vetor[8]))
            print("----------")
            print("%s | %s | %s" %(vetor[3],vetor[4],vetor[5]))
            print("----------")
            print("%s | %s | %s" %(vetor[0],vetor[1],vetor[2]))
            cont = 20
    cont += 1
