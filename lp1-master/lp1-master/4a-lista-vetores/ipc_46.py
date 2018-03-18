condicao = True
while condicao:
    atleta = str(input("Atleta: "))

    primeiro_salto = float(input("Primeiro salto: "))
    segundo_salto = float(input("Segundo salto: "))
    terceiro_salto = float(input("Terceiro salto: "))
    quarto_salto = float(input("Quarto salto: "))
    quinto_salto = float(input("Quinto salto: "))

    melhor_salto = primeiro_salto
    pior_salto = primeiro_salto

    if melhor_salto > segundo_salto:
        melhor_salto = melhor_salto
    else:
        melhor_salto = segundo_salto
    if pior_salto < segundo_salto:
        pior_salto = pior_salto
    else:
        pior_salto = segundo_salto

    if melhor_salto > terceiro_salto:
        melhor_salto = melhor_salto
    else:
        melhor_salto = terceiro_salto
    if pior_salto < terceiro_salto:
        pior_salto = pior_salto
    else:
        pior_salto = terceiro_salto

    if melhor_salto > quarto_salto:
        melhor_salto = melhor_salto
    else:
        melhor_salto = quarto_salto
    if pior_salto < quarto_salto:
        pior_salto = pior_salto
    else:
        pior_salto = quarto_salto

    if melhor_salto > quinto_salto:
        melhor_salto = melhor_salto
    else:
        melhor_salto = quinto_salto
    if pior_salto < quinto_salto:
        pior_salto = pior_salto
    else:
        pior_salto = quinto_salto

    print ("\nMelhor salto: ",melhor_salto,"m")
    print ("Pior salto: ",pior_salto,"m")

    soma = primeiro_salto + segundo_salto + terceiro_salto + quarto_salto + quinto_salto
    media_saltos_restantes = ((soma - (melhor_salto + pior_salto))/3)
    print("Média dos demais saltos: %1.1f" % media_saltos_restantes,"m")

    print ("\nResultado final:")
    print (atleta,": %1.1f" % media_saltos_restantes,"m")

    uso = 0
    while uso == 0:
        uso = input("\nInformar outro atleta? S-sim/N-não \n")
        if uso == "S" or uso == "s":
            condicao = True
        elif uso == "N" or uso == "n":
            condicao = False
        else:
            print ("Valor invalido!")
            uso = 0
