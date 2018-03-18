#Monitor: Lucas Botinelly
#Thiago Santos Borges - 1615310023
#Antonio Rodrigues de Souza Neto - 1615310028

def mostrar_matriz(matriz, m):
    for i in range(m):
        print(matriz[i])
        
matriz = [[0,-1,0,-1,-1,0,-1,0],[0,0,0,0,-1,0,0,0],[0,0,-1,-1,0,0,-1,0],[-1,0,0,0,0,-1,0,0],[0,0,-1,-1,0,0,-1,-1]]
linha = len(matriz)
coluna = len(matriz[0])

cont  = 0
for i in range(linha):
    for j in range(coluna):
        if matriz[i][j] != -1:
            if j == (coluna - 1):
                if matriz[i + 1][j] != -1:
                    cont += 1
                    matriz[i][j] = cont
            elif matriz[i][j + 1] != -1:
                cont += 1
                matriz[i][j] = cont


mostrar_matriz(matriz,linha)
