"""A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio           123456456
carlos              91257581
cesar               987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal."""
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


    
