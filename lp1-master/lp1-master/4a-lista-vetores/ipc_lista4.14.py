pergunta = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?"
,"Já trabalhou com a vítima?"]
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
