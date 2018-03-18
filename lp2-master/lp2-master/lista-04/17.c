#include <stdio.h>
/* Criar uma função que calcule o número de combinações de n elementos p a p. A fórmula da combinação é a seguinte: 
 
C =    n! 
    P!*(n-p)! */

float combinacao(int n,int p);
int fat(int num);
int main(int argc, char** argv)
{
	int n,p;
	printf("Informe o valor de n e p: ");
	scanf("%d %d",&n,&p);
	if(n < p){
		printf("Valor invalido, digite n maior ou igual a p");
	}
	else {
		float comb = combinacao(n,p);
		printf("Combinacao de n elementos p a p e = %.2f",comb);	
	}
	return 0;
}

float combinacao(int n,int p){
	float combi;
	combi = fat(n)/(fat(p)*fat(n-p));
	return combi;
}

int fat(int num){
	int fatorial=1,i;
	for(i = num;i > 0;i--){
		fatorial *= i; 
	}
	return fatorial;
}