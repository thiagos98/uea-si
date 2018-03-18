altura=float(input("Altura(m)="))
sexo=int(input("Qual seu sexo?[1-m] e [2-f]"))

if (sexo==1):
    pesoideal=(72.7*altura)-58
elif(sexo==2):
    pesoideal=(62.1*altura)-44.7
else:
    print("Digite uma das opções válidas.")

print("Peso Ideal para sua altura:",pesoideal,"kg")

peso=float(input("Agora, informe o seu peso(kg):"))
if (peso > pesoideal+5):
    print("Acima do peso.")
elif (peso < pesoideal-5):
    print("Abaixo do peso.")
else:
    print("Dentro do peso.")


