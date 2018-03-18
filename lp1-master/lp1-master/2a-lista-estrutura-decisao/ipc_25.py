contevid = 0

prop1 = input("Telefonou para a vítima? [s/n]")
if prop1 == "s":
    contevid = contevid + 1

prop2 = input("Esteve no local do crime? [s/n]")
if prop2 == "s":
    contevid = contevid + 1

prop3 = input("Mora perto da vítima? [s/n]")
if prop3 == "s":
    contevid = contevid + 1

prop4 = input("Devia para a vítima? [s/n]")
if prop4 == "s":
    contevid = contevid + 1

prop5 = input("Já trabalho com a vítima? [s/n]")
if prop5 == "s":
    contevid = contevid + 1

if contevid < 2:
    print("INOCENTE")
elif contevid == 2:
    print("SUSPEITA")
elif contevid > 2 and contevid < 5:
    print("CÚMPLICE")
else:
    print("ASSASSINO")
