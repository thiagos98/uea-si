preco_1 = float(input("Preço 1: R$"))
preco_2 = float(input("Preço 2: R$"))
preco_3 = float(input("Preço 3: R$"))

if preco_1 < preco_2 and preco_1 < preco_3:
    print("Compre o produto com preço 1! Preço: R$%.2f" %preco_1)
elif preco_2 < preco_1 and preco_2 < preco_3:
    print("Compre o produto com preço 2! Preço: R$%.2f" %preco_2)
elif preco_3 < preco_1 and preco_3 < preco_2:
    print("Compre o produto com preço 3! Preço: R$%.2f" %preco_3)
