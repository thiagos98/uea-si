from datetime import datetime

now = datetime.now()
COMECO = now.minute,now.second

cont = 0
for i in range(10000000000):cont += 1

atual = now.minute,now.second


print(COMECO)
print(atual)
