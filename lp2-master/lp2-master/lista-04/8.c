#include <stdio.h>

int verificar_idade(idade);
int main(int argc, char** argv)
{
	int idade;
	printf("Informe a idade do nadador: ");
	scanf("%d",&idade);
	if(verificar_idade(idade) == 1) {
		printf("Infantil A");
	}
	else if(verificar_idade(idade) == 2) {
		printf("Infantil B");
	}
	else if(verificar_idade(idade) == 3) {
		printf("Juvenil A");
	}
	else if(verificar_idade(idade) == 4) {
		printf("Juvenil B");
	}
	else if(verificar_idade(idade) == 5) {
		printf("Adulto");
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