#include<stdio.h>
#define tam 10


/*Escreva um programa que lê um vetor V(20) e o escreve. Compacte, a seguir, este vetor, 
retirando dele todos os valores nulos ou negativos e escreva o vetor compactado. 
Compacte o vetor ainda mais, retirando agora os elementos em duplicata. Escreva o vetor final*/

int vetor[tam];

void lerVetor(){
	int i;
	for(i = 0;i < tam; i++){
		printf("V[%d]: ",i+1);
		scanf("%d",&vetor[i]);
	}
}

void imprimirVetor(){
	int i;
	printf("Vetor\n");
	for(i = 0;i < tam; i++){
		printf("%d   ",vetor[i]);
	}
}

void verificarNumeros(){
	int i;
	for(i = 0;i < tam; i++){
		if(vetor[i] == 0){
			retirarNulo(i);
		} else if(vetor[i] < 0){
			retirarNegativo(i);
		}
	}
}
void retirarNulo(int indice){
	for (int i = indice; i < length; i++){
		vetor[] = array[index+1];
		array[length-1] = NULL;	
	}
}

void retiraDuplicata(){
	int i,j,k,n=tam;
	for(i = 0;i < n;i++){
		for(j = i + 1;j < n;j++){
			if(vetor[i] == vetor[j]){
				for(k = j + 1; k < n;k++){
					vetor[k-1] = vetor[k];
				}
				n--;
			}
		}
	}
}