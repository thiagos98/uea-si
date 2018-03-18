/*Construa um algoritmo que leia a quantidade de dinheiro existente no caixa de uma empresa (CAIXA), 
a quantidade de produtos a ser comprada (QTD) e o preço de cada unidade (PR). 
Caso o valor total da compra seja superior a 80% do valor em caixa, a compra deve ser feita a prazo (3x), 
com juros de 10% sobre o valor total. Caso contrário, a compra deverá ser realizada a vista, 
onde a empresa receberá 5% de desconto. 
Apresentar a forma de pagamento escolhida e o valor a ser pago (total a vista ou total a prazo), 
dependendo da escolha realizada pelo programa*/

#include <stdio.h>
#include <string.h>

int main(int argc, char** argv)
{
	float caixa,punitario,total;
	int quant;
	char pagamento[20];
	
	printf("Dinheiro existente no caixa: R$");
	scanf("%f",&caixa);
	printf("Quantidade de produtos: ");
	scanf("%d",&quant);
	printf("Preco Unitario do Produto: R$");
	scanf("%f",&punitario);
	
	total = punitario * quant;
	if (total > (caixa + caixa*0.8))
	{
		total += total*0.1;
		total /= 3;
		strcpy(pagamento,"A prazo(x3)");
	}
	else
	{
		total -= total*0.05;
		strcpy(pagamento,"A vista");
	}
	
	printf("Forma de pagamento: %s",pagamento);
	printf("\nValor a ser pago: R$%.2f",total);
	return 0;
}