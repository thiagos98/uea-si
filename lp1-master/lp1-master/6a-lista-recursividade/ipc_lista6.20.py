#coding: utf-8
""" Um fatorial exponencial é um inteiro positivo N elevado à potência de N-1, que por sua vez é elevado à potência
de N-2 e assim em diante. Ou seja, n^(n-1)^(n-2)^...  
Faça uma função recursiva que receba um número inteiro positivo N e retorne o fatorial exponencial desse número"""

def fat(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fat(numero - 1)
     

def fat_exponencial(numero):
    if numero == 0:
        return 1
    else:
        return numero ** fat(numero - 1)

numero = int(input("Fatorial Exponencial\nDigite o numero: "))
fatexp = fat_exponencial(numero)
print("Fatorial exponencial de %d é %d"%(numero,fatexp))
