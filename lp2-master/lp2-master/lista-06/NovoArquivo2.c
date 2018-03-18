#include <stdio.h>
#include <string.h>

imprimeAritPonteiro(char *nome);
imprimeIndexMatriz(char *nome);

int main(){
	char nome[20];
	printf("Digite nome: ");
	scanf("%s",nome);
	printf("\n\n");
	imprimeAritPonteiro(nome);
	printf("\n\n");
	imprimeIndexMatriz(nome);
}

imprimeAritPonteiro(char *nome){
	int i;
	for(i=0;nome[i];i++){
		putchar(nome[i]);
	}
}

imprimeIndexMatriz(char *nome){
	while(*nome){
		putchar(*nome++);
	}
}