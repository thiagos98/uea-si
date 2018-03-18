/*Os editores de texto possuem um recurso que permite o usuário substituir 
	uma sub-cadeia de um texto por outra cadeia de caracteres. 
	Escreva um programa que realize esta ação numa frase dada*/
	
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void escrever_arq(char cadeia[]);

void criar_arq(){
	FILE *arq;
	arq = fopen("questao03.txt","w");
	if(arq == NULL){
		printf("Nao foi possivel criar o arquivo");
		exit(1);
	}
	
	char cadeia[] = "Terminal da Matriz, na rua 15 de novembro, 1990. Registro de video produzido por Rick Ray. Jogando fifa 17 com os amigos da rua";
	
	fputs(cadeia,arq);
	
	fclose(arq);
}

void ler_arq(){
	FILE *arq;
	arq = fopen("questao03.txt","r");
	
	if(arq == NULL){
		printf("Erro! Nao foi possivel abrir o arquivo");
		exit(1);
	}
	
	char cadeia[1000];
	fgets(cadeia,200,arq);
	
	escrever_arq(cadeia);
	
	fclose(arq);
}

void escrever_arq(char cadeia[]){
	int i,indicein,indicefi;
	FILE *arq;
	arq = fopen("resp03.txt","w");
	char subcadeia[] = "na avenida 7 de setembro jogando pes 17 com esses patos";
	if(arq == NULL){
		printf("Erro! Nao foi possivel abrir o arquivo");
		exit(1);
	}
	
	char cadeiacopia[strlen(cadeia)];
	strcpy(cadeiacopia,cadeia);
	
	for(i=0;i<strlen(cadeia);i++){
		printf("%d ",i);
	}
	printf("\n%s",cadeia);
	printf("\n\nIndice Inicial e Final para troca de strings: ");
	scanf("%d %d",&indicein,&indicefi);
	while(indicefi - indicein != strlen(subcadeia)){
		printf("\nInforme um intervalo com tamanho minimo de %d!",strlen(subcadeia));
		scanf("%d %d",&indicein,&indicefi);
	}
	int j=0;
	for(i=indicein;i<=indicefi;i++){
		cadeiacopia[i] = subcadeia[j];
		j++;
	}
	
	for(i=indicefi;i<strlen(cadeia);i++){
		cadeiacopia[i] = cadeia[i];
	}
	
	fputs(cadeiacopia,arq);
	
	fclose(arq);
}

int main(int argc, char** argv){
	criar_arq();
	ler_arq();
	return 0;
}