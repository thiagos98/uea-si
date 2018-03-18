area=float(input("Área que vai ser pintada em metros quadrados:"))
litros=area/6
print("Quantidade de litros necessários:",litros,"L")
print("--PREÇOS FINAIS E QUANTIDADES--")

latas = litros / 18
parte_dec1=abs(latas) - abs(int(latas))
if (parte_dec1 != 0):
    latas = 1 + abs(latas-parte_dec1)
preco18 = latas*80
print(" Somente latas de 18L:",latas,".Preço: R$",preco18)

galoes=litros/3.6
parte_dec2 = abs(galoes) - abs(int(galoes))
if (parte_dec2!=0):
    galoes=abs(galoes-parte_dec2)+1
preco36=galoes*25
print(" Somente galões de 3.6L:",galoes,".Preço: R$",preco36)

if (galoes > 3):
    print("Misturando latas e galões,",galoes,"galoes e",latas,"latas.")
    print("Preço: R$",(galoes*80)+(latas*25))
    


