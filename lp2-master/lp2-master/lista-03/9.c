#include<stdio.h>
#include <conio.h>
//Faça um algoritmo para:
//a) Ler um valor x qualquer
//b) Calcular Y = ( x+1)+(x+2)+(x+3)+(x+4)+(x+5)+...(x+100).

int main()
{
	int i,x,expressao = 0;
	printf("Informe o valor de x: ");
	scanf("%d",&x);
	for (i = 1;i < 3;i++)
	{
		expressao += x + i;	
	}
	printf("Valor da Expressao e: %d",expressao);
	getch();
	return 0;
}