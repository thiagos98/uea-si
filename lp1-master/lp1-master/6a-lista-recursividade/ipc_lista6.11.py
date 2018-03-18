#coding: utf-8
"""A multiplicação de dois números inteiros pode ser feita através de somas sucessivas.
Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros"""

def multrec(num1,num2):
    if num1 == 0:
        return 0
    else:
        return num2 + multrec(num1 - 1,num2)

num1 = int(input("Digite num1: "))
num2 = int(input("Digite num2: "))
produto = multrec(num1,num2)

print(produto)
