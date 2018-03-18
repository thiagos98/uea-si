import time
import os

def tempo():
    for m in range(2):
        for s in range(60):
            time.sleep(1)
            #Comando para limpar tela            
            os.system("cls")
            print("%i:%i" %(m,s))
            tempo = m,s
    print("tempo recorde: "%tempo)
    hgddf = input()
tempo()
