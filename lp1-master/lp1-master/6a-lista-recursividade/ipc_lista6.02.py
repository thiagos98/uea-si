#coding: utf-8
"""Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência
Fibonacci"""

def fib(numero):
    if numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
        return fib(numero - 1) + fib(numero - 2)
    
print("Termo da sequencia Fibonacci")
num = int(input("Digite numero: "))

fibonacci = fib(num)

print("O %do termo da sequencia Fibonacci é %d"%(num,fibonacci))
