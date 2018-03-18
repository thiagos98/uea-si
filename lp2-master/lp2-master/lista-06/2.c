/*Faça uma rotina que recebe uma matriz A(5,6) de reais e retorna um vetor M 
	com os maiores valores de cada linha de A.*/
	
#include <stdio.h>
#define linha 2
#define coluna 3


float m[linha][coluna],v[linha];
int k=0;

void verificarMaior(int i);
void lerMatriz(){
	int i,j;
	for(i=0;i<linha;i++){
		for(j=0;j<coluna;j++){
			printf("M[%d][%d]: ",i+1,j+1);
			scanf("%f",&m[i][j]);
		}
	}
}
void maiorValor(){
	int i;
	for(i=0;i<linha;i++){
		verificarMaior(i);
	}
}

void verificarMaior(int i){
	int j,maior;
	for(j=0;j<coluna;j++){
		if(j == 0){
			maior = m[i][j];	
		} else if(m[i][j] >= maior){
			maior = m[i][j];
		}
	}
	v[k] = maior;
	k++;
}

void imprimir(){
	int i,j;
	printf("Matriz\n");
	for(i=0;i<linha;i++){
		for(j=0;j<coluna;j++){
			printf("%.1f  ",m[i][j]);
		}
		printf("\n");
	}
	printf("\n\nVetor\n");
	for(j=0;j<linha;j++){
		printf("%.1f  ",v[j]);
	}
}

int main(int argc, char** argv){
	lerMatriz();
	maiorValor();
	imprimir();
	return 0;
}