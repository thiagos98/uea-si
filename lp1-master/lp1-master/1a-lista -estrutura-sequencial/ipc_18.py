#
#Thiago Santos Borges
#Lorene Marques
#Nadine Brito
#Alexandre Souza
#

tamanho_arq = float(input("Digite o tamanho do arquivo(MB):"))
velocidade = float(input("Informe a velocidade da sua internet(Mbps):"))

tamanho_mbps = tamanho_arq * 8
tempo_seg = tamanho_mbps / velocidade
tempo_min = tempo_seg / 60
print("O tempo de download é %.2f" %tempo_min ," minutos")
