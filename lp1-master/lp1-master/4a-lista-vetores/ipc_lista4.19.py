"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos."""

sistema = ["1-Windows Server             ","2-Unix                       ","3-Linux                      ","4-Netware                    ","5-Mac OS                     ","6-Outro                      "]
soma = windows = unix = linux = netware = mac = outro = 0
twindows = tunix = tlinux = tmetware = tmac = toutro = 0
cond = True
taxas = []
contvotos = []
maior = 0
votos = 0
nome = ""

def taxa (dado1,dado2):
   return (dado1 * 100) / dado2
    
for i in sistema:
    print(i) 

while cond:
    voto = int(input("Informe valor de 1-6(0=sair):"))
    if voto == 1:
        windows = windows + 1
        soma = soma + 1
       # twindows = taxa(windows,soma)
    elif voto == 2:
        unix = unix + 1
        soma = soma + 1
        #tunix = taxa(unix,soma)
    elif voto == 3:
        linux = linux + 1
        soma = soma + 1
     #   tlinux = taxa(linux,soma)
    elif voto == 4:
        netware = netware + 1
        soma = soma + 1
      #  tnetware = taxa(netware,soma)
    elif voto == 5:
        mac = mac + 1
        soma = soma + 1
       # tmac = taxa(mac,soma)
    elif voto == 6:
        outro = outro + 1
        soma = soma + 1
        #toutro = taxa(outro,soma)
    elif voto == 0:
        cond = False
    else:
        print("Informe um valor valido!")

twindows = taxa(windows,soma)
tunix = taxa(unix,soma)
tlinux = taxa(linux,soma)
tnetware = taxa(netware,soma)
tmac = taxa(mac,soma)
toutro = taxa(outro,soma)

taxas.append(twindows)
taxas.append(tunix)
taxas.append(tlinux)
taxas.append(tnetware)
taxas.append(tmac)
taxas.append(toutro)

contvotos.append(windows)
contvotos.append(unix)
contvotos.append(linux)
contvotos.append(netware)
contvotos.append(mac)
contvotos.append(outro)

for i,k,p in zip(sistema,contvotos,taxas):
    if p >= maior:
        nome = i
        votos = k
        maior = p
print(" - Sistema Operacional     -     Votos     -     %     - ")
for i,k,p in zip(sistema,contvotos,taxas):
    print("%s     %d             %.2f"%(i,k,p))
print("\nTotal                             %d"%soma)

print("O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.2f dos votos."%(nome,votos,maior))






