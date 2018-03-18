#
#Kylciane Cristiny Lopes Freitas - 1615310052
#Thiago Santos Borges - 1615310023
#
import random


cond = True

pedra = 1
papel = 2
tesoura = 3
spock = 4
lagarto = 5

print("Vamos brincar de Jokenpo?")
print("Digite seu nome")
nome = input()

print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
print("4 - Spock")
print("5 - Lagarto")


tentativa = int(input("Digite uma face\n"))
while cond:
    bot  = random.randrange(1,4)
#############################################################
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
    elif tentativa == lagarto and bot == lagarto:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Empate!!!")
    elif tentativa == spock and bot == spock:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Empate!!!")

###########################################################
        
    elif tentativa == pedra and bot == papel:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nPapel cobre pedra")
    elif tentativa == pedra and bot == spock:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nSpock vaporiza a pedra")
    elif tentativa == pedra and bot == tesoura:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nPedra quebra tesoura")
    elif tentativa == pedra and bot == lagarto:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nPedra esmaga lagarto")
    
##############################################################

    elif tentativa == papel and bot == tesoura:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nTesoura corta papel")
    elif tentativa == papel and bot == lagarto:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nLagarto come papel")
    elif tentativa == papel and bot == pedra:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nPapel cobre pedra")
    elif tentativa == papel and bot == spock:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nPapel refuta spock")

################################################################

    elif tentativa == tesoura and bot == pedra:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nPedra quebra tesoura")
    elif tentativa == tesoura and bot == spock:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nSpock quebra tesoura")
    elif tentativa == tesoura and bot == papel:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nTesoura corta papel")
    elif tentativa == tesoura and bot == lagarto:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nTesoura decapita lagarto")
        
##################################################################

    elif tentativa == spock and bot == lagarto:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nLagarto envenena spock")
    elif tentativa == spock and bot == papel:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nPapel refuta spock")
    elif tentativa == spock and bot == tesoura:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nSpock quebra tesoura")
    elif tentativa == spock and bot == pedra:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nSpock vaporiza a pedra")

###################################################################

    elif tentativa == lagarto and bot == pedra:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nPedra esmaga lagarto")
    elif tentativa == lagarto and bot == tesoura:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Derrota!!!\nTesoura decapita lagarto")
    elif tentativa == lagarto and bot == papel:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nLagarto come papel")
    elif tentativa == lagarto and bot == spock:
        print(nome+": ",tentativa)
        print("Robo : ",bot)
        print("Vitoria!!!\nLagarto envenena spock")

###################################################################
    resp = str(input("Deseja jogar novamente??\n"))
    if resp == "n":
        cond = False
    else:
        cond = True
        tentativa = int(input("Digite uma face\n"))

    
