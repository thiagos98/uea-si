ano = int(input("Digite o ano para verificacao:"))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("Ano é bissexto!")
else:
    print("Não é bissexto!")
