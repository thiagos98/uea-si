/* Escreva uma função que exclua os comentários de um programa da linguagem C.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void retira_coment(char codigo[]);
void ler_arq(){
	FILE *arq;
	arq = fopen("questao05.txt","r");
	if(arq == NULL){
		printf("Erro! Nao foi possivel ler o arquivo");
		exit(0);
	}
	
	char codigo[200];
	
	while(fgets(codigo,200,arq) != NULL){
		retira_coment(codigo);
	}
	
	fclose(arq);
}

void retira_coment(char codigo[]){
	FILE *arq;
	arq = fopen("resp05.txt","a");
	if(arq == NULL){
		printf("Nao foi possivel criar o arquivo!");
		exit(1);
	}
	
	int i=0,j=0,k=0;
	while(codigo[i] != '\n'){
		if((codigo[i] == '/' && codigo[i+1] == '/') || (codigo[i] == '/' && codigo[i+1] == '*')){
			j = i;
			while(codigo[j] != '\n'){
				codigo[j] = ' ';
				j++;
			}		
		} else if(codigo[i] == '/' && codigo[i+1] == '*'){
			k = i+1;
			while(k >= 0){
				codigo[k] = ' ';
				k--;
			}
			/*else if(codigo[i] == '*' && codigo[i+1] == '/'){
			k = i+1;
			while(k >= 0){
				codigo[k] = ' ';
				k--;
			}*/
		}
		i++;
	}
	/* || (codigo[i] == '/' && codigo[i+1] == '*') || (codigo[i] == '*' && codigo[i+1] == '/')*/
	fputs(codigo,arq);
	
	fclose(arq);
}

int main(int argc, char** argv){
	ler_arq();
	return 0;
}