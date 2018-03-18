/*Escreva uma função recursiva que calcule a soma dos elementos positivos do vetor de inteiros v[0..n-1]. 
	O problema faz sentido quando n é igual a 0? 
	Quanto deve valer a soma nesse caso?*/
	
#include <stdio.h>
#define tam 5

int v[tam];

void lerVetor(){
	int i;
	for(i=0;i<tam;i++){
		printf("V[%d]: ",i+1);
		scanf("%d",&v[i]);
	}
}

int soma(int ind){
	if(ind == (tam - 1)){
		return v[tam - 1];
	} else {
		if(v[ind] >= 0){
			return v[ind] + soma(ind + 1);
		} else {
			return soma(ind + 1);
		}
	}
}

int main(int argc, char** argv){
	int s=0;
	lerVetor();
	s = soma(0);
	printf("%d",s);
	return 0;
}