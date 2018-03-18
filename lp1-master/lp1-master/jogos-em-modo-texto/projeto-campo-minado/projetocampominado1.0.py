import random
import string

def criarmatriz():
    matriz = [[0 for i in range(16)] for i in range(16)]
    matrizminas = gerarminas(matriz)
    return matrizminas

def gerarminas(matriz):
    for i in range(40):
        linha = random.randint(0,15)
        coluna = random.randint(0,15)
        valor = -1
        if matriz[linha][coluna] == -1:
            linha = random.randint(0,15)
            coluna = random.randint(0,15)
            valor = -1
            matriz[linha][coluna] = valor
        else:
            matriz[linha][coluna] = valor
    
    return verificar_entorno_casa(matriz)

def verificar_entorno_casa(matriz):
    for i in range(16):
        for j in range(16):
            if matriz[i][j] == -1:
                for posicao in range(8):
                    if(posicao == 0) and verificar_posicao_valida(matriz, i - 1, j - 1) and matriz[i-1][j-1] != -1:
                        matriz[i - 1][j - 1] += 1
                    if(posicao == 1) and verificar_posicao_valida(matriz, i - 1, j) and matriz[i-1][j] != -1:
                        matriz[i - 1][j] += 1
                    if(posicao == 2) and verificar_posicao_valida(matriz, i - 1, j + 1) and matriz[i-1][j+1] != -1:
                        matriz[i - 1][j + 1] += 1
                    if(posicao == 3) and verificar_posicao_valida(matriz, i, j + 1) and matriz[i][j+1] != -1:
                        matriz[i][j + 1] += 1
                    if(posicao == 4) and verificar_posicao_valida(matriz, i + 1, j + 1) and matriz[i+1][j+1] != -1:
                        matriz[i + 1][j + 1] += 1
                    if(posicao == 5) and verificar_posicao_valida(matriz, i + 1, j) and matriz[i+1][j] != -1:
                        matriz[i + 1][j] += 1
                    if(posicao == 6) and verificar_posicao_valida(matriz, i + 1, j - 1) and matriz[i+1][j-1] != -1:
                        matriz[i + 1][j - 1] += 1
                    if(posicao == 7) and verificar_posicao_valida(matriz, i, j - 1) and matriz[i][j-1] != -1:
                        matriz[i][j - 1] += 1
    return matriz

def verificar_posicao_valida(matriz, linha, coluna):     
    if(linha < 0):
        return False
    elif(linha >= len(matriz)):
        return False
    elif(coluna < 0):
        return False
    elif(coluna >= len(matriz[0])):
        return False
    else:
        return True

def mostrartabuleiro(grade):
    gradetam = len(grade)
    horizontal = "   "+4*gradetam*"-"+"-"
    label = "     "
    for i in string.ascii_lowercase[:gradetam]:
        label = label+i+'   '
    print (label+"\n"+horizontal)
    for idx,i in enumerate(grade):
        linha = "{0:2} |".format(idx+1)
        for j in i:
            linha = linha+" "+str(j)+" |"
        print (linha+"\n"+horizontal)
    print ("")

def obtervizinhos(grade,linha,coluna):
    gradetam = len(grade)
    row = grade[linha]
    column = grade[linha][coluna]

    vizinho = []

    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0: continue
            elif -1<linha+i<gradetam and -1<coluna+j<gradetam:
                vizinho.append((linha+i,coluna+j))
    return vizinho

def mostrarcelulas(grade,campo,linha,coluna):
    if campo[linha][coluna]!=" ":
        return

    campo[linha][coluna] = grade[linha][coluna]

    if grade[linha][coluna] == 0:
        for r,c in obtervizinhos(grade,linha,coluna):

            if campo[r][c] != "F" and grade[r][c] != -1:
                mostrarcelulas(grade,campo,r,c)

def jogarnovamente():
    print("Deseja jogar novamente(s/n)?")
    resp = str(input())
    if resp == "s":
        return True
    else:
        return False

def jogargame():
    flag = False
    flags = []
    campo = [[' ' for i in range(16)] for i in range(16)]
    mostrartabuleiro(campo)
    print("Digite a coluna, depois pela linha (ex.: a5).\n")
    while True:
        grade_minas = criarmatriz()
        celula = str(input("Entre com a celula[letranumero]: "))
        celula = (int(celula[1:3])-1,string.ascii_lowercase.index(celula[0]))
        linha,coluna = celula
        if grade_minas[linha][coluna] == -1:
            print ("Game Over\nSeu Noob")
            mostrartabuleiro(grade_minas)
            if jogarnovamente(): jogargame()
            else: exit()
        else:
            mostrarcelulas(grade_minas,campo,linha,coluna)

        mostrartabuleiro(campo)

jogargame()
