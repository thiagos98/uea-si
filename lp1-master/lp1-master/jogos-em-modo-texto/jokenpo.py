#
#Kylciane Cristiny Lopes Freitas - 1615310052
#Thiago Santos Borges - 1615310023
#
import random


cond = True

pedra = 1
papel = 2
tesoura = 3

print("Vamos brincar de Jokenpo???")
print("Digite seu nome")
nome = input()

print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")


tentativa = int(input("Digite uma face\n"))
while cond:
    bot  = random.randrange(1,4)
    if tentativa == pedra and bot == pedra:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Empate!!!")
    elif tentativa == papel and bot == papel:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Empate!!!")
    elif tentativa == tesoura and bot == tesoura:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Empate!!!")
    elif tentativa == pedra and bot == papel:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!")
    elif tentativa == pedra and bot == tesoura:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!")
    elif tentativa == papel and bot == tesoura:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!")
    elif tentativa == papel and bot == pedra:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!")
    elif tentativa == tesoura and bot == pedra:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!")
    elif tentativa == tesoura and bot == papel:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!")
    resp = str(input("Deseja jogar novamente??\n"))
    if resp == "n":
        cond = False
    else:
        cond = True
        tentativa = int(input("Digite uma face\n"))

    
