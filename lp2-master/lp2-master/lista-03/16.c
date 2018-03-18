/*Faça um algoritmo para encontrar o fatorial de um número lido. */

#include <stdio.h>
#include <conio.h>

int main(int argc, char** argv){
	int i,fat = 1,num;
	printf("Informe o numero para calcular o fatorial: ");
	scanf("%d",&num);
	for (i = num;i > 0;i--){
		fat *= i;	
	}
	printf("O fatorial de %d e = %d",num,fat);
	getch();
	return 0;
}