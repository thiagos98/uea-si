#coding: utf-8
"""A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1
até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15.
Faça uma função recursiva que receba um número inteiro positivo
impar N e retorne o fatorial duplo desse número. """

def fat_duplo(numero):
    if numero == 0:
        return 1
    elif numero == 1:
        return numero
    elif numero % 2 != 0:
        return numero * fat_duplo(numero - 2)
        

numero = int(input("Digite um numero natural impar: "))
if numero % 2 == 0:
    print("Numero informado é invalido")
else:
    fatorial_duplo = fat_duplo(numero)
    print("Fatorial duplo de %d é "%numero,fatorial_duplo)
    
