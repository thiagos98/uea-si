#include <stdio.h>
#include <conio.h>

int main(int argc, char** argv){
	int soma = 0,num = 101,den = 0,fat=1;
	int n,cont = 0,i;
	printf("Informe N: ");
	scanf("%d",&n);
	while(cont<n){
		if(den == 0){
			fat = 1;
		}
		else{
			for (i = den;i > 0;i--){
				fat *= i;
			}	
		}
		
		soma += (num - 1)/fat;
		cont += 1;
		den += 1;
	}
	printf("O valor da S para N = %d e: %d",n,soma);
	getch();
	return 0;
}