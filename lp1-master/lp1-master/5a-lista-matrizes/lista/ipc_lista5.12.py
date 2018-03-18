#monitor: Delrick Oliveira
#Thiago Santos Borges - 1615310023
#Antonio Rodrigues de Souza Neto - 1615310028

def cadastro(funcio):
    auxiliar=[]
    funcionario = []
    for i in range(funcio):
        nome=input("Digite o nome do funcionario %d:"%i)
        auxiliar.append(nome)
        salario=int(input("Digite o salario do funcionario %d:"%i))
        auxiliar.append(salario)
        hed=int(input("Digite as horas extras diurnas do funcionario %d:"%i))
        auxiliar.append(hed)
        hen=int(input("Digite as horas extras noturnas do funcionario %d:"%i))
        auxiliar.append(hen)
        nd=int(input("Digite o numero de dependentes do funcionario %d:"%i))
        auxiliar.append(nd)
        fal=int(input("Digite o numero de faltas em horas do funcionario %d:"%i))
        auxiliar.append(fal)
        descontos=int(input("Digite os descontos eventuais do funcionario %d:"%i))
        auxiliar.append(descontos)
        refe=int(input("Digite os gastos com refeiçoes feitas na empresa do funcionario %d:"%i))
        auxiliar.append(refe)
        val=int(input("Digite o vales retirados durante o mes do funcionario %d:"%i))
        auxiliar.append(val)
        funcionario.append(auxiliar)
        auxiliar =[]
    return funcionario

def mostrar(funcionario):
    for i in range(len(funcionario)):
        hora_extra = funcionario[i][2]*funcionario[i][1]/160+funcionario[i][3]*1.2*funcionario[i][1]/160
        sal_familia = funcionario[i][4]*0.05*800
        sal_bruto = funcionario[i][1] + hora_extra + sal_familia
        print("Nome:",funcionario[i][0])
        print("Salario: R$%d"%funcionario[i][1])
        print("horas extras: R$%.2f"%hora_extra)
        print("Salario familia: R$%.2f"%sal_familia)
        print("salario bruto: R$%.2f"%sal_bruto)
        print("Descontos efetuados")
        inamps = 0.08 * funcionario[i][1]
        faltas = funcionario[i][5]*(funcionario[i][1]/160)
        refeicoes = funcionario[i][7]
        vales = funcionario[i][8]
        descontos = funcionario[i][6]
        impostorenda = 0.08 * sal_bruto
        desc_total = inamps + faltas + refeicoes + vales + descontos + impostorenda
        sal_liquido = sal_bruto - desc_total
        print("inamps:R$%.2f"%inamps)
        print("faltas:R$%.2f"%faltas)
        print("refeicoes:R$%.2f"%refeicoes)
        print("vales:R$%.2f"%vales)
        print("descontos eventuais:R$%.2f"%descontos)
        print("imposto de renda:R$%.2f"%impostorenda)
        print("SALARIO LIQUIDO:R$%.2f"%sal_liquido)

funcio=int(input("Digite quantos funcionários são:"))
funcionario = cadastro(funcio)
mostrar(funcionario)
