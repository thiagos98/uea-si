/* Construa um algoritmo que calcule o novo salário (SAL_NOVO) de um funcionário. 
Considere que o funcionário deverá receber um reajuste de 15% caso seu salário (SAL) seja menor que 500. 
Se o salário for maior ou igual a 500, mas menor ou igual a 1000, o reajuste deve ser de 10%. 
Caso o salário seja maior que 1000, o reajuste deve ser de 5%*/

#include <stdio.h>
#define QUINZE 0.15
#define DEZ 0.1
#define CINCO 0.05

int main(int argc, char** argv)
{
	float salario,novo_salario;
	int reajuste;
	
	printf("Digite o seu salario: R$");
	scanf("%f",&salario);
	
	if (salario < 500)
	{
		novo_salario = salario + (salario * QUINZE);
		reajuste = 15;
	}
	else if (salario >= 500 && salario <= 1000)
	{
		novo_salario = salario + (salario * DEZ);
		reajuste = 10;
	}
	else
	{
		novo_salario = salario + (salario * CINCO);
		reajuste = 5;
	}
	
	printf("O reajuste do seu salario foi de %d(por cento)",reajuste);
	printf("\nPassou de R$%.2f para R$%.2f",salario,novo_salario);
	return 0;
}