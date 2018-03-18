/*Faça uma rotina que recebe duas matrizes A(2,3) e B(3,4) e retorna uma matriz 
C que é o produto matricial de A por B. */

#include <stdio.h>
#define l1 2
#define c1 3
#define l2 3
#define c2 4

int m1[l1][c1],m2[l2][c2];

void lerMatriz(){
	int i,j;
	for(i=0;i<l1;i++){
		for(j=0;j<c1;j++){
			printf("M1[%d][%d]: ",i+1,j+1);
			scanf("%d",&m1[i][j]);
		}
	}
	printf("\n\n");
	for(i=0;i<l2;i++){
		for(j=0;j<c2;j++){
			printf("M2[%d][%d]: ",i+1,j+1);
			scanf("%d",&m2[i][j]);
		}
	}
}

int multi_matriz(){
	int i,j,k,acm,mp[l1][c2];
	for(i=0;i<l1;i++){
		for(j=0;j<c2;j++){
			acm = 0;
			for(k=0;k<l2;k++){
				acm += m1[i][k] * m2[k][j];
			}
			mp[i][j] = acm;
		}
	}
	printf("\n\n");
	for(i=0;i<l1;i++){
		for(j=0;j<c2;j++){
			printf("%d ",mp[i][j]);
		}
		printf("\n");
	}
}

int main(int argc, char** argv){
	lerMatriz();
	multi_matriz();
	return 0;
}

