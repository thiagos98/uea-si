#include <stdio.h>
#include <conio.h>
int main(int argc, char** argv)
{
	int numero,n = 1,soma = 0;
	while(1){
		printf("Informe numero: ");
		scanf("%d",&numero);
		while((n < numero) && (numero%2 == 0)){
			if (numero%n == 0){
				soma += n;
				printf("Divisores: %d\n",n);
			}
			n += 1;
		}
		printf("Soma = %d\n",soma);
		if (soma == numero){
			printf("E perfeito\n");
		}
		else{
			printf("Nao e perfeito\n");
		}
		soma = 0;
		n = 1;
	}
	getch();
	return 0;
}