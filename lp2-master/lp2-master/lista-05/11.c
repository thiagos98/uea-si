#include<stdio.h>
#define tam 9

/* Seja um vetor inteiro de 9 elementos: 
a) preencher por leitura o vetor (apenas valores positivos > 0); 
b) imprimir os elementos do vetor; 
c) liberar a primeira posição do vetor deslocando todos os valores de uma posição (o último valor será perdido nesse processo). Escrever o vetor; 
d) somar o índice de cada elemento ao conteúdo do mesmo. Escrever o vetor; 
e) ler um valor e imprimir o número de ocorrências desse valor no vetor. 
*/

int vetor[tam],cont;

void lerVetor(){
	int i;
	for(i = 0; i < tam; i++){
		printf("x[%d]: ",i+1);
		scanf("%d",&vetor[i]);
		while(vetor[i] < 1){
			scanf("%d",&vetor[i]);
		}
	}
}
void imprimirVetor(){
	int i;
	for(i = 0;i < tam; i++){
		printf("%d   ",vetor[i]);
	}
}

void liberarVetor(){
	int num,i;
	printf("\n\nDigite o proximo numero do vetor: ");
	scanf("%d",&num);
	for(i = (tam-1); i > -1; i--){
		if(i){
			vetor[i] = vetor[i - 1];
		} else {
			vetor[i] = num;	
		}
	}
}

void somarIndice(){
	int i;
	for(i = 0;i < tam;i++){
		vetor[i] += i;
	}
}

int numOcorrencias(){
	int i,x;
	cont = 0;
	printf("\nNumero para ser verificado: ");
	scanf("%d",&x);
	for(i = 0; i < tam;i++){
		if(vetor[i] == x){
			cont++;
		}
	}
	return x;
}

int main(int argc, char** argv)
{
	int nume;
	lerVetor();
	imprimirVetor();
	liberarVetor();
	imprimirVetor();
	somarIndice();
	printf("\n\nIndices Somados: ");
	imprimirVetor();
	nume = numOcorrencias();
	printf("O numero de ocorrencias do numero %d no vetor e de %d vezes",nume,cont);
	return 0;
}