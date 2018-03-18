import random
LIMITE = 25
def separacao_questoes():
    questao = random.randrange(LIMITE)
    return questao

for i in range(6):    
    print(separacao_questoes())