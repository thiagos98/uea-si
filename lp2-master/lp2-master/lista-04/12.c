#include <stdio.h>

/* Faça um procedimento que recebe, por parâmetro, um valor N e calcula e 
escreve a tabuada de 1 até N. Mostre a tabuada na forma*/

void tabuada(int numero);
int main(int argc, char** argv)
{
	int numero;
	printf("Informe o valor de N: ");
	scanf("%d",&numero);
	tabuada(numero);
	return 0;
}

void tabuada(int numero){
	int i,tab;
	printf("\nCasa de %d",numero);
	for(i=1;i<11;i++){
		tab = i*numero;
		printf("\n%d*%d = %d",i,numero,tab);
	}
}