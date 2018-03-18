#coding: utf-8
""" O fatorial quádruplo de um número N é dado por (2*n)!/n! 
Faça uma função recursiva que receba um número inteiro positivo N e retorne o fatorial quádruplo desse número"""

def fat(numero):
    if numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        return numero * fat(numero - 1)
def fat_quad(numero,duplo):
    if numero == 1 or duplo == 1:
        return 1
    else:
        return fat(duplo)/fat(numero)

numero = int(input("Formula (2n)!/n!.\nDigite n: "))
duplo = numero * 2
quad = fat_quad(numero,duplo)
print("Fatorial quádruplo: ",quad)
