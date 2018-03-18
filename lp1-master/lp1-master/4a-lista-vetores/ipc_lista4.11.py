vetor1 = []
vetor2 = []
vetor3 = []
vetorint = []

print("Numeros do vetor 1")
for i in range(10):
    vetor1.append(int(input("Digite numero:")))

print("Numeros do vetor 2")
for i in range(10):
    vetor2.append(int(input("Digite numero:")))

print("Numeros do vetor 3")
for i in range(10):
    vetor3.append(int(input("Digite numero:")))

for i,p,k in zip(vetor1,vetor2,vetor3):
    vetorint.append(i)
    vetorint.append(p)
    vetorint.append(k)

print("Vetor 1:",vetor1)
print("Vetor 2:",vetor2)
print("Vetor 3:",vetor3)

print("\nVetor intercalado:",vetorint)
