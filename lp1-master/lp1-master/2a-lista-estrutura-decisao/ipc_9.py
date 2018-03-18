numero_1 = float(input("numero 1:"))
numero_2 = float(input("numero 2:"))
numero_3 = float(input("numero 3:"))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("1o:",numero_1)
    if numero_2 > numero_3:
        print("2o:",numero_2)
        print("3o:",numero_3)
    else:
        print("2o:",numero_3)
        print("3o:",numero_2)

if numero_2 > numero_1 and numero_2 > numero_3:
    print("1o:",numero_2)
    if numero_1 > numero_3:
        print("2o:",numero_1)
        print("3o:",numero_3)
    else:
        print("2o:",numero_3)
        print("3o:",numero_1)

if numero_3 > numero_2 and numero_3 > numero_1:
    print("1o:",numero_3)
    if numero_2 > numero_1:
        print("2o:",numero_2)
        print("3o:",numero_1)
    else:
        print("2o:",numero_1)
        print("3o:",numero_2)
