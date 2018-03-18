/*Ler uma matriz A (MxN) de elementos inteiros. 
	Gerar uma matriz B (NxN+1) da seguinte maneira: 
	Os elementos da coluna N+1 são formados pela multiplicação do menor pelo maior elemento de cada linha. 
	Faça M = 3 e N = 3. */
	
#include<stdio.h>
#define tam 3


int mA[tam][tam],mB[tam][tam+1];
void gerarColuna(int i);
void lerMatriz(){
	int i,j;
	printf("\nMatriz A\n");
	for(i=0;i<tam;i++){
		for(j=0;j<tam;j++){
			printf("M[%d][%d]: ",i+1,j+1);
			scanf("%d",&mA[i][j]);
	    }	
	}
	printf("\nMatriz B\n");
	for(i=0;i<tam;i++){
		for(j=0;j<tam+1;j++){
			if(j == 3){
				gerarColuna(i);
			} else {
				printf("M[%d][%d]: ",i+1,j+1);
				scanf("%d",&mB[i][j]);	
			}	
		}
	}
}

void gerarColuna(int i){
	int j,maior,menor;
	for(j=0;j<tam;j++){
		if(j==0){
			maior = menor = mB[i][j];
		} else if(mB[i][j] >= maior) {
			maior = mB[i][j];
		} else if(mB[i][j] <= menor){
			menor = mB[i][j];
		}
	}
	mB[i][tam] = maior*menor;
}

void imprimir(){
	int i,j;
	printf("Matriz A:\n");
	for(i=0;i<tam;i++){
		for(j=0;j<tam;j++){
			printf("%d  ",mA[i][j]);
		}
		printf("\n");
	}
	printf("Matriz B:\n");
	for(i=0;i<tam;i++){
		for(j=0;j<tam+1;j++){
			printf("%d  ",mB[i][j]);
		}
		printf("\n");
	}
}
int main(int argc, char** argv){
	lerMatriz();
	printf("\n\n");
	imprimir();
	return 0;
}