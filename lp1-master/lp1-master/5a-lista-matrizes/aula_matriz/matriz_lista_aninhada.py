matriz3x3 = [[0,1,8],
             [4,7,5],
             [8,4,6]]

for i in range(3):
    print(matriz3x3[i])

for i in range(3):
    for j in range(3):
        print("Elemento %d%d ->"%(i+1,j+1),matriz3x3[i][j])
