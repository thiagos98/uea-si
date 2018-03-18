#include <stdio.h>
#include <conio.h>

int main(int argc, char** argv){
	int x,n;
	float y = 0;
	int i,j;
	printf("Digite o valor de x(espaco)n: ");
	scanf("%d %d",&x,&n);
	
	for (i=1;i<=n;i++){
		int prod = 1;
		for (j = 1; j < (i+1);j++){
			prod = prod*j;	
		}
		y += (x+i)/prod;
	}
	
	printf("%f",y);
	return 0;
}