import re
def cpf(s):
    #s = "581.612.159-60"
    verificacao = False
    
    for simb in s:
        if simb == '-':
            s = s.replace('-','')
        elif simb == '.':
            s = s.replace('.','')
    ###################################3
    lista = [i for i in range(11)]
    listaNova = [0 for i in range(len(lista))]

    for valor,indice in zip(s,lista):
        if s[indice].isdigit():
            listaNova[indice] = int(s[indice])
        else:
            return False
    ########################################
    soma = 0
    digito1 = 0
    digito2 = 0
    lista1 = [10,9,8,7,6,5,4,3,2]
    lista2 = [11,10,9,8,7,6,5,4,3,2]
    #########################################
    for valor1,i in zip(lista1,listaNova):
        soma += valor1*i
        
    div = soma//11
    resto = soma%11

    if resto < 2:
        digito1 = 0
    elif resto >= 2:
        digito1 = 11 - resto

    
    #################################
    soma = 0
    for valor2,i in zip(lista2,listaNova):
        soma += valor2*i

    div = soma//11
    resto = soma%11

    if resto < 2:
        digito2 = 0
    elif resto >= 2:
        digito2 = 11 - resto

    
    ###################################
    if listaNova[9] == digito1 and listaNova[10] == digito2:
        return True
    else:
        return False
    

def senha(s):
    for simb in s:
        if(simb == '.'):
            s = s.replace('.',' ')
    verif = True
    if s[0] == s[1]:
        verif = False
    """elif s[6] == s[7]:
        verif = False
    elif s[9] == s[10]:
        verif = False
    """
    return verif

def vapp(s):
    
    for simb in s:
        if(simb == '.'):
            s = s.replace('.',' ')
    versaoApp = s.split()

    #modificado
    lista = [0 for i in range(2)]

    #IndexError: list index out of range
    if type(versaoApp[0]) is str:
        if versaoApp[0] == "ubuntu" or versaoApp[0] == "login" or versaoApp[0] == "windows" or versaoApp[0] == "Xubuntu" or versaoApp[0] == "ios":
            return False
        else:
            lista[0] = int(versaoApp[0])

    if type(versaoApp[1]) is str:
        lista[1] = int(versaoApp[1])
    #modificado
    if(lista[0] < lista[1]):
        return False
    else:
        return True
    
    

try:
    verificarEntrada = True
    verificarCpf = False
    verificarSenha = False
    verificarVapp = False

    stringDeEntrada = str(input())
        
    #################################################
    dados = stringDeEntrada.split()
    verificarCpf = cpf(dados[1])
    verificarSenha = senha(dados[3])
    verificarVapp = vapp(dados[5])
    ################################################
    padrao = re.search(r'^[a-z][a-zA-Z]+\s+\d{3}\.\d{3}\.\d{3}\-\d{2}\s+[a-zA-z\.-_][\w\.-_]+@\w+\.[\w\.]+\s+[A-F\d]{2}\.[A-F\d]{2}\.[A-F\d]{2}\.[A-F\d]{2}\s+[\w\-\.]+\s+\d+\.\d+\s+[windows|mac|ios|linux|android|windowsPhone]+\s*$|^[a-z][a-zA-Z]+\s+\d{3}\.\d{3}\.\d{3}\-\d{2}\s+[a-zA-z][\w\.-]+@\w+\.[\w\.]+\s+[A-F\d]{2}\.[A-F\d]{2}\.[A-F\d]{2}\.[A-F\d]{2}\s+[\w\-\.]+\s+\d+\.\d+\s+[windows|mac|ios|linux|android|windowsPhone]+\s+([a-zA-Z]+\s+[a-zA-z][\w\.-]+@\w+\.[\w\.]+\s*){1,}$',stringDeEntrada)

    verificacao = False
    if(padrao and verificarCpf and verificarSenha and verificarVapp and verificarEntrada):
        verificacao = True
    else:
        SystemExit

    print(verificacao)
except:
    print(False)