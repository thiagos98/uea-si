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
