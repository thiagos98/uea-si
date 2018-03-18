/*Faça uma rotina que recebe uma matriz A(4,4) de reais e retorna o seu maior e 
	o seu menor valor. */
	
#include <stdio.h>

#define tam 2

float m[tam][tam];

void lerMatriz(){
	int i,j;
	for(i=0;i<tam;i++){
		for(j=0;j<tam;j++){
			printf("M[%d][%d]: ",i+1,j+1);
			scanf("%f",&m[i][j]);
		}
	}
}

void verificarMaiorMenor(){
	int i,j;
	float maior = m[0][0];
	float menor = maior;
	for(i=0;i<tam;i++){
		for(j=0;j<tam;j++){
			if(m[i][j] >= maior) {
				maior = m[i][j];
			} else if (m[i][j] <= menor){
				menor = m[i][j];
			}
		}
	}
	printf("Maior: %.2f\nMenor: %.2f",maior,menor);
	//return maior;
}

int main(int argc, char** argv){
	//float maior=0;
	//float *m;
	lerMatriz();
	verificarMaiorMenor();
//	printf("Maior: %.2f\nMenor: %.2f",maior,*m);
	return 0;
}