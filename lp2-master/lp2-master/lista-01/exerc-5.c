/*5.	Faça um algoritmo que leia o nome e as idades de duas pessoas e mostre a soma das idades*/

#include <stdio.h>

int main(int argc, char** argv)
{
	int soma,idade1,idade2;
	char nome1[10],nome2[10];
	
	printf("Idades: ");
	scanf("%d %d",&idade1,&idade2);
	printf("Nomes: ");
	scanf("%s %s",nome1,nome2);
	
	soma = idade1 + idade2;
	
	printf("Nomes: %s %s",nome1,nome2);
	printf("\nIdades: %d %d",idade1,idade2);
	printf("\nSoma: %d",soma);
	return 0;
}