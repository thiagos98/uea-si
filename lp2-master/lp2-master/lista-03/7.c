#include<stdio.h>
#include <conio.h>
//Criar um algoritmo que leia um número e imprima todos os números de 1 até o número lido e o seu produto

int main()
{
	int i,prod = 1;
	int limite;
	scanf("%d",&limite);
	
	for (i = 1; i < (limite+1);i++)
	{
		prod = prod*i;	
	}
	printf("Produto: %d",prod);	
	getch();
	return 0;
}