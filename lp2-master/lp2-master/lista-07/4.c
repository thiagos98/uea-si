/* Escreva uma função recursiva que computa até o N-ésimo elemento da série Fibonacci. 
A série de Fibonacci é formada de maneira que o elemento seguinte é composto 
pela soma dos 2 elementos anteriores: 1, 1, 2, 3, 5, 8, 13, 21*/

#include <stdio.h>

int fibon(int num){
	if(num == 0 || num == 1){
		return 1;
	}
	return fibon(num - 1) + fibon(num - 2);
}

int main(int argc, char** argv){
	int num;
	int fib = 0;
	printf("Informe N: ");
	scanf("%d",&num);
	fib = fibon(num);
	printf("O %d-esimo termo da serie de fibonacci e %d",num,fib);
	return 0;
}