class Stack:
    def __init__(self):
        self.itens = []

    def push(self,item):
        self.itens.append(item)

    def pop(self):
        return self.itens.pop()

    def isEmpty(self):
        return (self.itens == [])

def casamento(lista):
    pilha = Stack()
    for dado in lista:
        if(dado == '(' or dado == '[' or dado == '{'):
            pilha.push(dado)
        elif(dado == ')' or dado == ']' or dado == '}' and not(pilha.isEmpty())):
            topo = pilha.pop()
            if not(testeRemoverPilha(topo,dado)):
                return False
        else:
            return False
    if pilha.isEmpty():
        return True

def testeRemoverPilha(topo,lista):
    var = False
    if topo == '(' and lista == ')':
        var = True
    elif topo == '[' and lista == ']':
        var = True
    elif topo == '{' and lista == '}':
        var = True
    return var

def validarEntrada(l):
    teste = True
    for dado in l:
        if (dado != '(' and dado != ')' and dado != '[' and dado != ']' and dado != '{' and dado != '}'):
            l = l.replace(dado,"")

    for dado in l:
        if (dado != '(' and dado != ')' and dado != '[' and dado != ']' and dado != '{' and dado != '}'):
            teste = False


    return teste,l

def fechado(l):
    contador = 0
    for dado in l:
        if dado == " ":
            contador += 1

    if contador == len(l):
        return False
    else:
        return True



try:
    strEntrada = str(input())
    validador,strEntrada = validarEntrada(strEntrada)
    validador2 = fechado(strEntrada)
    if(validador and casamento(strEntrada) and validador2):
        print(True)
    else:
        print(False)
except:
    print(True)