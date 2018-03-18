/*No dia da estréia do filme “Senhor dos Anéis”, uma grande emissora de TV realizou uma pesquisa logo após o encerramento do filme. 
Cada espectador respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme: excelente -3; bom-2; regular-1. 
Criar um algoritmo que receba a idade e a opinião de 20 espectadores, calcule e imprima: 
a) a média das idades das pessoas que responderam excelente; 
b) a quantidade de pessoas que responderam regular; 
c) a percentagem de pessoas que responderam bom entre todos os expectadores analisados. */

#include <stdio.h>
#include <conio.h>

int main(int argc, char** argv){
	int i;
	int opiniao,idade,contExc = 0,contReg = 0,acmId = 0;
	float medA = 0,percentBom = 0,contBom = 0;
	printf("Filme: Senhor dos Aneis\n1-Regular\n2-Bom\n3-Excelente\n");
	for (i=0;i < 5;i++){
		printf("\nInforme a sua opiniao sobre o filme conforme o menu acima: ");
		scanf("%d",&opiniao);
		printf("Agora, informe a sua idade: ");
		scanf("%d",&idade);
		if (opiniao == 3){
			contExc += 1;
			acmId += idade;
		}
		else if (opiniao == 2){
			contBom += 1;
		}
		else if (opiniao == 1){
			contReg += 1;
		}
		else if (opiniao != 1 && opiniao != 2 && opiniao != 3){
			printf("Informe uma opcao valida!");
			i -= 1;
		}
	}
	medA = acmId/contExc;
	percentBom = (contBom/5.0)*100;
	printf("A media das idades de quem respondeu 'Excelente': %.2f\nA quantidade de pessoas que responderam regular: %d\nA porcentagem de pessoas que responderam 'Bom': %.2f",medA,contReg,percentBom);
	getch();
	return 0;
}