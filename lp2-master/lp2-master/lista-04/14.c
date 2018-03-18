#include <stdio.h>

/*Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.  
S = 1 + 1/1! + ½! + 1/3! + ...+ 1 /N! */

float calc_exp(int numero);
int fat(int num);
int main(int argc, char** argv)
{
	int numero;
	printf("Digite valor de N: ");
	scanf("%d",&numero);
	float S = calc_exp(numero);
	printf("O valor da expressao e %.2f",S);
	return 0;
}

float calc_exp(int numero){
	int i=1;
	float s=0;
	while(i <= numero){
		s += 1.0/fat(i);
		i++;
	}
	s += 1;
	return s;
}

int fat(int num){
	int i,fatorial=1;
	for(i=num;i>0;i--){
		fatorial *= i;
	}
	return fatorial;
}