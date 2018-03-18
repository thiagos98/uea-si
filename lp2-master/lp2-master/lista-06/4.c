/*Elabore uma rotina que recebe uma matriz A(5,6) de inteiros e 
	retorna um vetor com os primos de A*/
	
#include <stdio.h>

#define l 2
#define c 3

int m[l][c];
int v[6];

int verificarPrimo(int num);
void lerMatriz(){
	int i,j;
	for(i=0;i<l;i++){
		for(j=0;j<c;j++){
			printf("M[%d][%d]: ",i+1,j+1);
			scanf("%d",&m[i][j]);
		}
	}
}

void criarVetor(){
	int i,j,k=0;
	for(i=0;i<l;i++){
		for(j=0;j<c;j++){
			if(verificarPrimo(m[i][j])){
				v[k] = m[i][j];
				printf("%d ",k);
				printf("%d",v);
				k++;
			}
		}
	}
}

int verificarPrimo(int num){
	int cont=0,i;
	for(i=1;i<=num;i++){
		if(num%i == 0){
			cont++;
		}
	}
	if(cont==2){
		return 1;
	} else {
		return 0;
	}
}

void imprimirMatriz(){
	int i,j;
	printf("\n\n");
	for(i=0;i<l;i++){
		for(j=0;j<c;j++){
			printf("%d  ",m[i][j]);
		}
		printf("\n");
	}
}

void imprimirVetor(){
	int i;
	printf("\n");
	for(i=0;i<l;i++){
	   	printf("%d  ",v[i]);
	}
}

int main(int argc, char** argv)
{
	lerMatriz();
	criarVetor();
	imprimirMatriz();
	imprimirVetor();
	return 0;
}