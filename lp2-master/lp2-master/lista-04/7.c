#include <stdio.h>

/*7. Faça uma função que verifique se um valor é perfeito ou não. 
Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio. 
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). 
A função deve retornar um valor booleano.  */

int num_perfeito(int numero);
int main(int argc, char** argv){
	int numero;
	printf("Informe um numero: ");
	scanf("%d",&numero);
	if(num_perfeito(numero) == 1){
		printf("Numero perfeito");
	}
	else {
		printf("Numero nao perfeito");
	}
	return 0;
}

int num_perfeito(int numero){
	int i,acm = 0;
	for(i = 1;i<numero;i++){
		if(numero%i == 0){
			acm += i;
		}
	}
	if(acm == numero){
		return 1;
	}
	else {
		return 0;
	}
}