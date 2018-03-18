import random
import string
import time

TAM_MATRIZ = 15
QUANT_MINAS = 15
CASAS_ENTORNO_MINA = 8
CINCO_MINUTOS = 300

def criar_matriz():
    matriz = [[0 for i in range(TAM_MATRIZ)] for i in range(TAM_MATRIZ)]
    matrizminas,minas = gerar_minas(matriz)
    return matrizminas,minas

def gerar_minas(matriz):
    minas=[]
    for i in range(QUANT_MINAS):
        linha = random.randint(0,(TAM_MATRIZ - 1))
        coluna = random.randint(0,(TAM_MATRIZ - 1))
        valor = "X"
        if matriz[linha][coluna] == "X":
            linha = random.randint(0,(TAM_MATRIZ - 1))
            coluna = random.randint(0,(TAM_MATRIZ - 1))
            valor = "X"
            matriz[linha][coluna] = valor
            minas.append((linha,coluna))
        else:
            matriz[linha][coluna] = valor
            minas.append((linha,coluna))
    return verificar_entorno_casa(matriz),minas

def verificar_entorno_casa(matriz):
    for i in range(TAM_MATRIZ):
        for j in range(TAM_MATRIZ):
            if matriz[i][j] == "X":
                for posicao in range(CASAS_ENTORNO_MINA):
                    if(posicao == 0) and verificar_posicao_valida(matriz, i - 1, j - 1) and matriz[i-1][j-1] != "X":
                        matriz[i - 1][j - 1] += 1
                    if(posicao == 1) and verificar_posicao_valida(matriz, i - 1, j) and matriz[i-1][j] != "X":
                        matriz[i - 1][j] += 1
                    if(posicao == 2) and verificar_posicao_valida(matriz, i - 1, j + 1) and matriz[i-1][j+1] != "X":
                        matriz[i - 1][j + 1] += 1
                    if(posicao == 3) and verificar_posicao_valida(matriz, i, j + 1) and matriz[i][j+1] != "X":
                        matriz[i][j + 1] += 1
                    if(posicao == 4) and verificar_posicao_valida(matriz, i + 1, j + 1) and matriz[i+1][j+1] != "X":
                        matriz[i + 1][j + 1] += 1
                    if(posicao == 5) and verificar_posicao_valida(matriz, i + 1, j) and matriz[i+1][j] != "X":
                        matriz[i + 1][j] += 1
                    if(posicao == 6) and verificar_posicao_valida(matriz, i + 1, j - 1) and matriz[i+1][j-1] != "X":
                        matriz[i + 1][j - 1] += 1
                    if(posicao == 7) and verificar_posicao_valida(matriz, i, j - 1) and matriz[i][j-1] != "X":
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

def mostrar_tabuleiro(grade):
    print("\n")
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

def obter_vizinhos(grade,linha,coluna):
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

def mostrar_celulas(grade,campo,linha,coluna):
    if campo[linha][coluna]!=" ":
        return

    campo[linha][coluna] = grade[linha][coluna]

    if grade[linha][coluna] == 0:
        for r,c in obter_vizinhos(grade,linha,coluna):

            if campo[r][c] != "F" and grade[r][c] != "X":
                mostrar_celulas(grade,campo,r,c)
def jogar_novamente():
    print("Deseja jogar novamente(s/n)?")
    resp = str(input())
    if resp == "s":
        return True
    else:
        return False

def jogar_game():
    ini = time.time()
    atu = time.time()
    tempo = atu - ini
    flags = []
    campo = [[' ' for i in range(TAM_MATRIZ)] for i in range(TAM_MATRIZ)]
    mostrar_tabuleiro(campo) 
    flag = False
    mensagem=("Digite a coluna, depois pela linha (ex.: a5).\nPara adicionar um sinalizador, basta colocar um s ou S, antes da celula (ex.: za5)\n")
    print(mensagem)
    grade_minas,minas = criar_matriz()
    while (tempo < CINCO_MINUTOS):
        celula = str(input("Entre com a celula: "))
        if celula[0]=="S" or celula[0]=="s":
            celula = (int(celula[2:4])-1,string.ascii_lowercase.index(celula[1]))
            linha,coluna = celula
            print(celula)
            if campo[linha][coluna] ==" ":
                campo[linha][coluna] ="S"
                flags.append((linha,coluna))
            elif campo[linha][coluna] =="S":
                campo[linha][coluna] =" "
                flags.append((linha,coluna))
            else:
                print("Nao e possivel por uma bandeira")
                
        else:    
            celula = (int(celula[1:3])-1,string.ascii_lowercase.index(celula[0]))
            linha,coluna = celula
            if grade_minas[linha][coluna] == "X":
                print ("\nGame Over\nSeu Noob")
                mostrar_tabuleiro(grade_minas)
                print("Seu tempo foi: %.2f"%tempo,"seg\nTempo Limite: 300 seg = 5 min")
                if jogar_novamente(): jogar_game()
                else: exit()
            else:
                mostrar_celulas(grade_minas,campo,linha,coluna)
                
        
        mostrar_tabuleiro(campo)
        tempo = atu - ini
        print("Seu tempo foi: %.2f"%tempo,"seg\nTempo Limite: 300 seg = 5 min")
        
        if set(flags)==set(minas):
            print ("Voce Venceu!")
            print("Seu tempo foi: %.2f"%tempo,"seg\nTempo Limite: 300 seg = 5 min")
            if jogar_novamente(): jogar_game()
            else: exit()
        atu = time.time()
        tempo = atu - ini
    print("fim de jogo")        

jogar_game()
