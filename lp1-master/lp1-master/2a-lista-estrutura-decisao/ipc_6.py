num1 = int(input("numero 1:"))
num2 = int(input("numero 2:"))
num3 = int(input("numero 3:"))

if num1 >= num2 and num1 >= num3:
    print("\nmaior:",num1)
elif num2 >= num1 and num2 >= num3:
    print("\nmaior:",num2)
else:
    print("\nmaior:",num3)

