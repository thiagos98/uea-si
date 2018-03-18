/*7.	Faça um algoritmo que leia valores para as variáveis A, B e C e mostre o 
resultado da seguinte expressão: (A - C) * B */

#include <stdio.h>

int main(int argc, char** argv)
{
	int resultado,a,b,c;
	
	scanf("%d %d %d",&a,&b,&c);
	
	resultado = (a - c)*b;
	printf("(A - C)*B = %d",resultado);
	return 0;
}