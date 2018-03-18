#coding: utf-8
""" Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N"""

def fat(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fat(numero - 1)


numero = int(input("Digite numero: "))
fatorial = fat(numero)

print("Fatorial de %d é %d."%(numero,fatorial))
