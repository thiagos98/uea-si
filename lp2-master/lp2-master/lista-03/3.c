#include<stdio.h>
//Imprimir os 100 primeiros pares

int main()
{	
	int i = 1,cont = 0;
	int teste = 1;
	while(teste)
	{
		if (i%2 == 0)
		{
			cont += 1;
			printf("\n%d",i);
		}
		if (cont == 100)
		{
			teste = 0;		
		}
		i += 1;
	}
	return 0;
}