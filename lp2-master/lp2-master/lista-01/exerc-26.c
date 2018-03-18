/*26.	Criar um algoritmo que leia o peso de uma pessoa, só a parte inteira, calcular e imprimir:
a) O peso da pessoa em gramas.
b) Novo peso, em gramas, se a pessoa engordar 12%.
*/

#include <stdio.h>
#define TAXA 0.12

int main(int argc, char** argv)
{
	float peso,novopeso;
	int pesoint;
	
	printf("Digite seu peso(g): ");
	scanf("%f",&peso);
	
	pesoint = (int) peso;
	novopeso = pesoint + (TAXA*pesoint);
	
	printf("Peso Normal: %d",pesoint);
	printf("\nPeso Engordando 12(por cento): %d",(int) novopeso);
	
	return 0;
}