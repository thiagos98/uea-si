#include <stdio.h>
#include <conio.h>
/*Fazer um algoritmo que calcule  escreva o valor de S onde:  
S = 1/N + 2/N-1 + 3/N-2 + ... + N-1/2 + N */
int main(int argc, char** argv){
	int n,i,num = 0,dec = 0;
	float s = 0;
	printf("Digite o valor de N: ");
	scanf("%d",&n);
	for (i = 1;i<=n;i++){
		if ((n - dec) > 0){
			s = (num+1)/(n-dec);
			dec += 1;
		}	
	}
	printf("S = %.2f",s);
	getch();
	return 0;
}