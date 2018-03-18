#include <stdio.h>
#include <conio.h>

int main(int argc, char** argv){
	float soma = 0;
	float n;
	for (n = 1;n<50;n++){
		soma += 1/n;
		printf("\n%.2f",soma);
	}
	printf("\n\nSoma: %.2f",soma);
	getch();
	return 0;
}