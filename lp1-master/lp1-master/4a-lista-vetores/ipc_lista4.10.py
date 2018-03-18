vetor1 = []
vetor2 = []
vetorint = []

print("Numeros do vetor 1")
for i in range(10):
    vetor1.append(int(input("Digite numero:")))

print("Numeros do vetor 2")
for i in range(10):
    vetor2.append(int(input("Digite numero:")))

for i,p in zip(vetor1,vetor2):
    vetorint.append(i)
    vetorint.append(p)

print("Vetor 1:",vetor1)
print("Vetor 2:",vetor2)

print("\nVetor intercalado:",vetorint)
