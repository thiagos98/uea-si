area_pint=float(input(" Área que vai ser pintada em metros quadrados:"))
litros=area_pint/3
print("- Quantidade de litros a ser usada:",litros,"L")
quant_galoes=litros/18
print("- Quantidade de galões necessários:",quant_galoes)
preco=quant_galoes*80
print("- Preço Final: R$",preco)

