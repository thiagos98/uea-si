/*A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são fornecidos pelo usuário;
 a partir daí, os termos são gerados com a soma ou subtração dos dois termos anteriores, 
 ou seja: Ai = Ai-1 + Ai-2 para i ímpar Ai = Ai-1 – Ai-2 para i par.
Criar um algoritmo que imprima os 10 primeiros termos da série de FETUCCINE*/

#include <stdio.h>
#include <conio.h>

int main(int argc, char** argv)
{
	int i,a1,a2,ai;
	printf("Digite A1: ");
	scanf("%d",&a1);
	printf("Digite A2: ");
	scanf("%d",&a2);
	printf("%d",a1);
	printf("\n%d",a2);
	for (i=3;i<11;i++)
	{
		if (i%2 == 0)
		{
			ai = a2 - a1;
		}
		else
		{
			ai = a2 + a1;
		}
		printf("\n%d",ai);
		a1 = a2;
		a2 = ai;
	}
	return 0;
}