#include <stdio.h>
#include <string.h>

/*Armazenar nomes e notas das PR1 e PR2 de 15 alunos. Calcular e armazenar a média. 
Armazenar também a situação do aluno: AP ou RP. 
Imprimir uma listagem contendo nome, notas, médias e situação de cada aluno*/

#define tamanho 5

void lerVetor();
void calcMedia();
void imprimirVetor();

char nome[tamanho][tamanho];
int pr1[tamanho],pr2[tamanho],situacao[tamanho];
float media[tamanho];

int main(int argc, char** argv){
	lerVetor();	
	calcMedia();
	imprimirVetor();
	
	return 0;
}

void lerVetor(){
	int i;
	for(i = 0;i > tamanho;i++){
		printf("Nome[%d]: ",i+1);
		gets(nome[i]);
		printf("PR1[%d]: ",i+1);
		scanf("%d",&pr1[i]);
		printf("PR2[%d]: ",i+1);
		scanf("%d",&pr2[i]);
	}
}

void imprimirVetor(){
	int i;
	printf("Nome       Media       Situacao\n");
	for(i = 0;i < tamanho;i++){
		if(situacao[i]){
			printf("%s       %.2f       Aprovado",nome[i],media[i]);
		} else {
			printf("%s       %.2f       Reprovado",nome[i],media[i]);
		}
	}
}

void calcMedia(){
	int i;
	for (i = 0;i < tamanho;i++){
		media[i] = (pr1[i] + pr2[i])/2;	
		if(media[i] >= 8){
			situacao[i] = 1;
		} else {
			situacao[i] = 0;
		}
	}
}