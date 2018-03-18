#include<stdio.h>
//Criar um algoritmo que imprima todos os números de 1 até 100 e a soma deles

int main()
{
	int i,soma = 0;
	for (i = 1;i < 101;i++)
	{
		printf("\n%d",i);
		soma += i;	
	}
	printf("Soma: %d",soma);
	return 0;
}