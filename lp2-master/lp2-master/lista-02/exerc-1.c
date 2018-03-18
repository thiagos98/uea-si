/* Construa um algoritmo que apresente o nome e o salário de dois funcionários, 
de acordo com os seguintes critérios: 
a) Salários que sejam maiores ou iguais a R$ 1000,00 e menores ou iguais a R$ 1500,00 
b) Funcionários pertencentes aos departamentos de produção ou engenharia. 
Obs: Os departamentos são reconhecidos pelas letras (P) Produção e (E) Engenharia São fornecidos o nome do funcionário (NF), 
o seu salário (SAL) e o departamento onde trabalha (DEP). */

#include <stdio.h>

int main(int argc, char** argv)
{
	char nome1[10],nome2[10],dep1[2],dep2[2];
	float salario1,salario2;
	
	printf("Func.1 - Informe seu nome: ");
	scanf("%s",nome1);
	printf("Func.1 - Informe seu salario: R$");
	scanf("%f",&salario1);
	printf("Func.1 - Informe seu departamento: ");
	scanf("%s",dep1);
	printf("Func.2 - Informe seu nome: ");
	scanf("%s",nome2);
	printf("Func.2 - Informe seu salario: R$");
	scanf("%f",&salario2);
	printf("Func.2 - Informe seu departamento: ");
	scanf("%s",dep2);
	
	if (salario1 >= 1000 && salario1 <= 1500)
	{
		printf("Funcionario: %s\nSalario: R$%.2f\nDepartamento: %s",nome1,salario1,dep1);
	}
	if (salario2 >= 1000 && salario2 <= 1500)
	{
		printf("Funcionario: %s\nSalario: R$%.2f\nDepartamento: %s",nome2,salario2,dep2);
	}
	return 0;
}