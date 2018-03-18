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
