#include <stdio.h>
/*Armazenar 15 números inteiros em um vetor NUM e imprimir uma listagem numerada
 contendo o número e uma das mensagens: par ou impar*/
 
 #define tamanho 5
 
 void lerVetor(int vetor[]);
 int separaVetor(int vetor[],int vTipo[]);
  void escreverVetor(int vetor[],int vTipo[]);
 
 int main(int argc, char** argv) {
	 int vetor[tamanho],vTipo[tamanho];
	 lerVetor(vetor);
	 separaVetor(vetor,vTipo);
	 escreverVetor(vetor,vTipo);
	 return 0;
 }
 
 void lerVetor(int vetor[]) {
	 int i;
	 for(i = 0;i < tamanho;i++){
		 printf("Vetor[%d]: ",i+1);
		 scanf("%d",&vetor[i]);
	 }
 }
 
 int separaVetor(int vetor[],int vTipo[]){
	 int i;
	 for(i = 0;i < tamanho;i++){
		 if(vetor[i] % 2 == 0){
			 vTipo[i] = 1;
		 } else {
			 vTipo[i] = 0;
		 }
	 }
 }
 
 void escreverVetor(int vetor[],int vTipo[]){
	 int i;
	 printf("\nVetor\n");
	 for(i = 0;i < tamanho;i++){
		 if(vTipo[i]){
			 printf("%d: Par\n",vetor[i]);
		 } else {
			 printf("%d: Impar\n",vetor[i]);
		 }
	 }
 }