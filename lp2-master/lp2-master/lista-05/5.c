#include <stdio.h>
/* Armazenar nome e salário de 20 pessoas. Calcular e armazenar o novo salário 
sabendo-se que o reajuste foi 8%. 
Imprimir uma listagem com nome e novo salário*/

#define tamanho 5
#define taxa 0.08

void lerVetor();
void calcSalario();
//
//
//
char nome[tamanho][tamanho];
float salario[tamanho],nSalario[tamanho];

int main(int argc, char** argv)
{	
	lerVetor();
	calcSalario();
	return 0;
}

void lerVetor(){
	int i;
	for(i = 0;i > tamanho;i++){
		printf("Nome[%d]: ",i+1);
		gets(nome[i]);
		printf("Salario[%d]: ",i+1);
		scanf("%f",&salario[i]);
	}
}

void calcSalario(){
	int i;
	for(i = 0;i < tamanho;i++){
		nSalario[i] += salario[i]*taxa;
	}
}