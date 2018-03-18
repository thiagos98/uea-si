#include <stdio.h>

int verificar_media(media);
int main(int argc, char** argv)
{
	float media;
	printf("Informe a media do aluno: ");
	scanf("%f",&media);
	if(verificar_media(media) == 1) {
		printf("Conceito D");
	}
	else if(verificar_media(media) == 2) {
		printf("Conceito C");
	}
	else if(verificar_media(media) == 3) {
		printf("Conceito B");
	}
	else if(verificar_media(media) == 4) {
		printf("Conceito A");
	}
	return 0;
}

int verificar_idade(idade){
	if(idade>4 && idade<8){
		return 1;
	}
	else if(idade>7 && idade<11){
		return 2;
	}
	else if(idade>10 && idade<14){
		return 3;
	}
	else if(idade>13 && idade<18){
		return 4;
	}
	else if(idade>17){
		return 5;
	}
}