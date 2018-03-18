#coding: utf-8
""" O superfatorial de um número N é definida pelo produto dos N primeiros fatoriais de N.
Assim, o superfatorial de 4 é sf(4) = 1! * 2! * 3! * 4! = 288.
Faça uma função recursiva que receba um número inteiro positivo N e retorne o superfatorial desse número"""

def fat(numero):
    if numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        return numero * fat(numero - 1)

def superfat(numero):
    if numero == 1:
        return 1
    else:
        return fat(numero) * superfat(numero - 1)

numero = int(input("Digite numero: "))
fatsuper = superfat(numero)
print("Super fatorial de %d é "%numero,fatsuper)
