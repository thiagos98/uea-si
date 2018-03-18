#include <stdio.h>

/* Criar um algoritmo que leia dois conjuntos de números inteiros, tendo cada um
 10 e 20 elementos e apresente os elementos comuns aos conjuntos. 
Lembre-se de que os elementos podem se repetir mas não podem parecer repetidos*/

#define tamanhoA 5
#define tamanhoB 10

void lerConjunto(int vetor[],int tamanho,int nConj);
void imprimirConjunto(int vetor[],int tam,int nConj);
int retirarRepetidos(int v[],int num,int identificador);

int main(int argc, char** argv)
{
	int conjA[tamanhoA],conjB[tamanhoB];
	lerConjunto(conjA,tamanhoA,1);
	lerConjunto(conjB,tamanhoB,0);
	retirarRepetidos(conjA,tamanhoA,1);
    retirarRepetidos(conjB,tamanhoB,0);
//	imprimirConjunto(conjA,tamanhoA,1);
//	imprimirConjunto(conjB,tamanhoB,0);
	return 0;
}

void lerConjunto(int vetor[],int tamanho,int nConj){
	int i;
	if(nConj){
		printf("Conjunto A\n");
	} else {
		printf("Conjunto B\n");
	}
	for(i = 0;i < tamanho;i++){
		printf("Vetor[%d]: ",i+1);
		scanf("%d",&vetor[i]);
	}
}

int retirarRepetidos(int v[],int num,int identificador){
	int i,j,k,n=num;
	for (i=0; i<n; i++) {
		for (j=i+1; j<n; j++){
    		if (v[i] == v[j]){
				for (k=j+1; k<n; k++)
					v[k-1] = v[k];
            	n--;
			}
	    } 
	}
	if(identificador){
		imprimirConjunto(v,n,1);	
	} else{
		imprimirConjunto(v,n,0);	
	}
}

void imprimirConjunto(int vetor[],int tam,int nConj){
	int i;
	if(nConj == 1){
		printf("Conjunto A\n");
	} else if(nConj == 0) {
		printf("\nConjunto B\n");
	} else {
		printf("Resultado Final");
	}
	for(i = 0;i < tam;i++){
		printf("%d   ",vetor[i]);
	}
}