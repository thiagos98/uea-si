"""
#####lista4.1#####
vetor = []
for i in range(1,6):
    numero = int(input("Digite numero:"))
    vetor.append(numero)
print(vetor)

#####lista4.2#####
vetor1 = []
vetor2 = []

for i in range(1,6):
    numero = int(input("Digite numero:"))
    vetor1.append(numero)

i = len(vetor1) - 1
while i >= 0:
    indice = vetor1[i]
    vetor2.append(indice)
    i = i - 1
print(vetor2)

#####lista4.3#####

notas = []
media = acm = 0

for i in range(1,5):
    notaind = float(input("Informe a nota:"))
    notas.append(notaind)
    acm = acm + notaind

media = acm / i
for i in notas:
    print("Notas:%.1f"%i)
print("A media e %.1f"%media)


#####lista4.4#####

consoantes = []
letras = []
acm = 0
for i in range(1,11):
    letraind = input("Digite letra:")
    letras.append(letraind)
    if letraind == "a" or letraind == "e" or letraind == "i" or letraind == "o" or letraind == "u":
        acm = acm
    else:
        acm = acm + 1
        consoantes.append(letraind)

print("%d consoantes foram lidas.\nElas sao as seguintes %s"%(acm,consoantes))

#####lista4.5#####
par = []
impar = []
numeros = []

for i in range(1,11):
    numero = int(input("Digite numero:"))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Numeros digitados->",numeros)
print("Numero digitados pares->",par)
print("Numero digitados impares->",impar)

#####lista4.6#####

media = []
acm = 0
cont = 1
acmmedia = 0
contmedia = 0
mediaind = 0
i = 1
while i < 5:
    print("%d° aluno"%i)
    cont = 1
    acm = 0
    acmmedia = 0
    mediaind = 0
    while cont < 5:
        nota = float(input("Informe a nota:"))
        acm = acm + nota
        cont = cont + 1
    acmmedia = acmmedia +acm
    mediaind = (acmmedia)/4
    media.append(mediaind)
    if mediaind >= 7:
        contmedia = contmedia + 1
    print("Media:",media[(i-1)])
    i = i + 1
print("Alunos APROVADOS:%d"%contmedia)

#####lista4.7#####
vetor = []
multi = 1
soma = 0

for i in range(1,6):
    dado = int(input("Informe o dado:"))
    vetor.append(dado)
    multi = multi * dado
    soma = soma + dado

print("O numeros informados foram:",vetor)
print("A soma:%d"%soma)
print("A multiplicacao:%d"%multi)


#####lista4.8#####

idade = []
altura = []
idadeinv = []
alturainv = []

for i in range(1,4):
    id_pessoa = int(input("Informe sua idade->"))
    alt_pessoa = float(input("Inform sua altura(m)->"))
    idade.append(id_pessoa)
    altura.append(alt_pessoa)

i = len(idade) - 1
while i >= 0:
    indice = idade[i]
    idadeinv.append(indice)
    i = i - 1

i = len(altura) - 1
while i >= 0:
    indice = altura[i]
    alturainv.append(indice)
    i = i - 1

print(idade)    
print(idadeinv)
print("\n",altura)
print(alturainv)


#####lista4.9#####

a = []
soma = 0
quadrado = 1

for i in range(1,4):
    numero = int(input("Informe numero:"))
    a.append(numero)

for i in a:
    quadrado = i**2
    soma = soma + quadrado

print("A soma dos quadrados dos elementos e %d"%soma)


#####lista4.10#####

vetor1 = []
vetor2 = []
vetorint = []

print("Numeros do vetor 1")
for i in range(10):
    vetor1.append(int(input("Digite numero:")))

print("Numeros do vetor 2")
for i in range(10):
    vetor2.append(int(input("Digite numero:")))

for i,p in zip(vetor1,vetor2):
    vetorint.append(i)
    vetorint.append(p)

print("Vetor 1:",vetor1)
print("Vetor 2:",vetor2)

print("\nVetor intercalado:",vetorint)

#####lista4.11#####
vetor1 = []
vetor2 = []
vetor3 = []
vetorint = []

print("Numeros do vetor 1")
for i in range(10):
    vetor1.append(int(input("Digite numero:")))

print("Numeros do vetor 2")
for i in range(10):
    vetor2.append(int(input("Digite numero:")))

print("Numeros do vetor 3")
for i in range(10):
    vetor3.append(int(input("Digite numero:")))

for i,p,k in zip(vetor1,vetor2,vetor3):
    vetorint.append(i)
    vetorint.append(p)
    vetorint.append(k)

print("Vetor 1:",vetor1)
print("Vetor 2:",vetor2)
print("Vetor 3:",vetor3)

print("\nVetor intercalado:",vetorint)

#####lista4.12#####

idade = []
altura = []
mediaalt = 0
IDADELIMITE = 13
QUANT_ALUNOS = 5
acm = 0
alt = 0

for i in range(QUANT_ALUNOS):
    idadeind = int(input("Informe sua idade:"))
    idade.append(idadeind)
    alturaind = float(input("Informe sua altura(m):"))
    altura.append(alturaind)
    alt = alt + alturaind
    
mediaalt = alt / QUANT_ALUNOS
for k,i in zip(idade,altura):
    if k > IDADELIMITE and i < mediaalt:
        acm = acm + 1
        
print("Total de alunos com mais de 13 anos que possuem altura menor que a media de altura dos alunos:%d"%acm)
#####lista4.13#####

mes = ["Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
tempmes = []
acm = 0
QUANT_MES = 12
medianual = 0

for i in range(12):
    temp = float(input("Temperatura media do mes de %s:"%mes[i]))
    tempmes.append(temp)
    acm = acm + temp

medianual = acm / QUANT_MES

print("Media anual:%d"%medianual)
for i in range(12):
    if tempmes[i] > medianual:
        print("%d - %s: %.1f"%(i+1,mes[i],tempmes[i])) 


#####lista4.14#####

pergunta = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
classificacao = ""
acm = 0

print("Respostas S ou s-sim // N ou n-nao")
for i in pergunta:
    resp = str(input(i))
    if resp == "s" or resp == "S":
        acm = acm + 1
    elif resp == "n" or resp == "N":
        acm = acm
    else:
        print("Informe resposta valida")

if acm < 3:
    classificacao = "suspeita"
elif acm > 2 and acm < 5:
    classificacao = "cumplice"
elif acm == 5:
    classificacao = "assassino"
else:
    classificacao = "inocente"

print("A pessoa entrevistada é %s"%classificacao)


#####lista4.15#####

acmacima = 0
acm7 = 0
acm = 0
soma = 0
media = 0
nota = 0
notas = []
notasinv = []

while nota != -1:
    nota = float(input("Informe sua nota: "))
    if nota == -1:
        acm = acm
        soma = soma
    else:
        notas.append(nota)
        acm = acm + 1
        soma = soma + nota
    
media = soma / acm

for i in notas:
    if i > media:
        acmacima = acmacima + 1
    elif i < 7:
        acm7 = acm7 + 1
        
for i in notas[::-1]:
    notasinv.append(i)
    
print("Foram lidos %d notas"%acm)
print("Notas:",notas)
print("Notas na ordem inversa:")
for i in notasinv:
    print(i)

print("A soma das notas:%d"%soma)
print("A media das notas:%.1f"%media)
print("Quantidade de notas acima da media:%d"%acmacima)
print("Quantidade de notas abaixo de 7:%d"%acm7)


#####lista4.17#####

saltos = []
sequencia = ["Primeiro","Segundo","Terceiro","Quarto","Quinta"]
media = 0
acm = 0

nome = raw_input("Atleta: ")
print("")
for k in range(5):
    salto = float(input("%s Salto:"%sequencia[k]))
    saltos.append(salto)
    acm = acm + salto

media = acm / 5
print("Resultado Final:\nAtleta: $s\nSaltos: %d - \nMedia dos saltos: %.1f m"%(nome,salto,media))

#####lista4.23#####
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

"""

