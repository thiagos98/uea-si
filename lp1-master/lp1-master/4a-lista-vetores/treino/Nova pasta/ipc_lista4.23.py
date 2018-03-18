#ipc_lista4.23
#Thiago Santos Borges - Matrícula - 1615310023
#
numeros = []

for i in range(1,7):
    numeros.append(i)  
usuarios = []
byte = 0
espacomegabyte = []
taxa = []
media = 0
soma = 0
FUNCIONARIOS = 6

def bytemegabyte (tamanho):
    tamanho = tamanho * 0.000001
    return tamanho

def porcento (dado1,dado2):
   return (dado1 * 100) / dado2

for i in range(FUNCIONARIOS):
    nome = str(input("Nome: "))
    usuarios.append(nome)
    byte = int(input("Tamanho de armazenamento em bytes: "))
    espacomegabyte.append(bytemegabyte(byte))

for i in espacomegabyte:
    soma = soma + i

for i in espacomegabyte:
    taxa.append(porcento((i),soma))

media = soma / FUNCIONARIOS
print("-"*50 + "\nNr."+" "*3+"Usuário"+" "*5+"Espaco utilizado"+" "*3+"% do uso")
for i,k,p,u in zip(numeros,usuarios,espacomegabyte,taxa):
    print("%d      %s       %.2fMB                 %.2f "%(i,k,p,u))

print("Espaço total ocupado: %.2fMB"%soma)
print("Espaço médio ocupado:%.2fMB"%media)
