#include <stdio.h>

int main(int argc, char** argv)
{
	float pe,precototal,parcela;
	int cp,quantparcela;
	printf("------------------------------------------------------------");
	printf("\n    1    | A vista em dinheiro ou cheque, com 10 de desconto");
	printf("\n    2    | A vista cartao de credito, com 5 de desconto");
	printf("\n    3    | Em 2 vezes, preco normal de etiqueta sem juros");
	printf("\n    4    | Em 3 vezes, preco de etiqueto com acrescimo de 10");
	printf("\nInforme o preco de etiqueta: R$");
	scanf("%f",&pe);
	printf("EScolha uma forma de pagamento, conforme a tabela acima: ");
	scanf("%d",&cp);
	if (cp == 1)
	{
		precototal = pe - pe*0.1;
	}
	else if (cp == 2)
	{
		precototal = pe - pe*0.05;
	}
	else if (cp == 3)
	{
		precototal = pe;
		parcela = pe/2;
		quantparcela = 2;
	}
	else if (cp == 4)
	{
		precototal = pe + pe*0.1;
		parcela = precototal/3;
		quantparcela = 3;
	}
	else
	{
		printf("Opcao Invalida");
	}
	
	if (cp == 1 || cp ==2)
	{
		printf("\n\nPreco Total: R$%.2f",precototal);	
	}
	else
	{
		printf("\n\nPreco Total: R$%.2f",precototal);
		printf("\nParcelas: R$%.2f",parcela);
		printf("\nQuant de parcelas: %d",quantparcela);
	}
		
	return 0;
}