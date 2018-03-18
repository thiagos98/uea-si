def inverter_numero(num, inverso):
    if num != 0:
        inverso = (inverso*10)+(num%10)
        return inverter_numero(num//10,inverso)
    else:
        return inverso       
num = int(input("digite o numero: "))
aux = num
inverso = inverter_numero(aux,0)
print("O inverso do numero %d é %d"%(num,inverso))


    

