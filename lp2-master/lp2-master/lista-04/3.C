#include <stdio.h>
#include <math.h>

int primo(int numero);
int main(int argc, char** argv) {
	int numero;
	printf("Informe um numero inteiro e positivo para o teste: ");
	scanf("%d",&numero);
	if (primo(numero)){
		printf("Numero primo");
	}
	else {
		printf("Numero nao primo");
	}
	return 0;
}

int primo(int numero) {
	int i,cont=0;
	for(i = 1;i <= numero;i++){
		if (numero % i == 0){
			cont++;
		}
	}
	if(cont == 2) {
		return 1;
	}
	else {
		return 0;
	}
}