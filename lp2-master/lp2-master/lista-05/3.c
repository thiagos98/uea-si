#include <stdio.h>

/*Criar um algoritmo que armazene em dois vetores nome e 
profissão de 20 pessoas em seguida imprima*/

#define tamanho 3

void lerVetor();
void imprimirVetor();

char vNome[tamanho][tamanho+50],vProfissao[tamanho][tamanho+50];

int main(int argc, char** argv){
	lerVetor();
	imprimirVetor();
	return 0;
}

void lerVetor(){
	int i;
	for(i = 0;i < tamanho;i++){
		printf("Nome[%d]: ",i+1);
		gets(vNome[i]);
		printf("Profissao[%d]: ",i+1);
		gets(vProfissao[i]);
	}
}

void imprimirVetor(){
	int i;
	printf("Nome       Profissao\n");
	for(i = 0;i < tamanho;i++){
		printf("\n%s       %s\n",vNome[i],vProfissao[i]);
	}
}