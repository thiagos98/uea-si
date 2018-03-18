/*As companhias de transportes aereos costumam representar os nomes dos 
	passageiros no formato ultimo sobrenome. 
	Por exemplo, o passageiro Carlos Drummond de Andrade seria indicado como Andrade/Carlos. 
	Escreva um programa que receba um nome e o escreva no formato acima.*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void escrever_arq(char unome[],char pnome[]);

void criar_arq(){
	FILE *arq;
	arq = fopen("questao4.txt","w");
	
	if(arq == NULL){
		printf("Nao foi possivel criar o arquivo.");
		exit(1);
	}
	
	char nome[] = "David Barbosa da Silva";
	/*printf("Informe seu nome completo: ");
	scanf("%s",nome);*/
	
	fputs(nome,arq);
	
	fclose(arq);
}

void ler_arq(){
	int i = 0;
	FILE *arq;
	
	arq = fopen("questao4.txt","r");
	if(arq == NULL){
		printf("Nao foi possivel abrir o arquivo.");
		exit(1);
	}
	
	char nome[100];
	//char pnome[20],aux1=0;
	int aux1=0;
	//char unome[20],aux2=0;
	int aux2=0;
	
	fgets(nome,100,arq);
	//pegando o primeiro nome
	while(nome[i] != ' '){//while para pegar o tamanho do primeiro nome
		i++;
	}
	aux1=i;
	char pnome[aux1];//cria vetor com primeiro nome
	i = 0;
	while(nome[i] != ' '){
		pnome[i] = nome[i];//adiciona caractere a caractere do nome no vetor primeiro nome
		i++;
	}
	//pegando o ultimo nome
	i = (strlen(nome)-1);
	while(nome[i] != ' '){
		i--;
		aux2++;
	}
	i = (strlen(nome)-1);
	char unome[aux2];
	aux2=0;
	while(nome[i] != ' '){
		unome[aux2] = nome[i];
		i--;
		aux2++;
	}
	strrev(unome);
	
	//imprimir
	escrever_arq(unome,pnome);
	fclose(arq);
}
void escrever_arq(char unome[],char pnome[]){
	FILE *arq;
	arq = fopen("resp04.txt","w");
	if(arq == NULL){
		printf("Nao foi possivel criar o arquivo");
		exit(1);
	}
	
	fputs(unome,arq);
	fputs("/",arq);
	fputs(pnome,arq);
	
	fclose(arq);
}
int main(int argc, char** argv){
	criar_arq();
	ler_arq();
	return 0;
}