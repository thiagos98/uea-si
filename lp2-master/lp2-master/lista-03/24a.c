#include <stdio.h>
#include <conio.h>

int main(int argc, char** argv){
	int soma = 0,n=0;
	for(n = 0;n<50;n++){
		soma += 2*n;
		printf("\n%d",soma);
	}
	printf("\n\nSoma: %d",soma);
	return 0;
}