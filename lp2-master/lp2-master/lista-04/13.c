#include <stdio.h>

/* Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor*/

int contador_div(int num);
int main(int argc, char** argv){
	int numero,div;
	printf("Informe um numero inteiro e positivo: ");
	scanf("%d",&numero);
	div = contador_div(numero);
	printf("O numero %d tem %d divisores.",numero,div);
	return 0;
}

int contador_div(int num){
	int cont=0,i;
	for(i = 1;i <= num;i++){
		if(num % i){
			continue;
		}
		else {
			cont++;
		}
	}
	return cont;
}