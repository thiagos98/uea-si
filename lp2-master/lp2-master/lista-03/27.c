/*Dado modelo, ano de fabricação, cor e placa de 1000 carros, faça um algoritmo que:  
modelo: 1-fiat palho,2-chevrolet celta,3-ford fusion,4-fiat uno,5-volkswagen gol
ano de fabricação: 1-2008,2-2009,3-2010,4-2011,5-2012
cor: 1-preto,2-branco,3-verde,4-prateado
a) Imprima quantos são, da cor verde e o percentual em relação ao total. 
b) Imprima quantos foram fabricados antes de 2010 e o percentual em relação ao total. 
c) Imprima quantos são FIAT PALIO e o percentual em relação ao total. 
d) Imprima quantos carros tem na placa o digito 5 e o percentual em relação ao total. 
Considere placas com seguinte formato “AANNNN”. */

#include <stdio.h>
#include <conio.h>
#include <string.h>
int main(int argc, char** argv){
	int i=0,modelo,ano,cor,contFP=0,contCV=0,cont10=0,cont5=0,controle,n=0;
	float percentverde,percent98,percentfp,percent5;
	char placa[7];
	printf("Quantos carros serao registrados?\n");
	scanf("%d",&controle);
	while(n<controle){
		printf("\n\nModelos: \n1-Fiat Palio\n2-Outros modelos\nInforme o modelo do carro: ");
		scanf("%d",&modelo);
		printf("\nInforme o ano de fabricacao: ");
		scanf("%d",&ano);
		printf("\nCor: \n1-verde\n2-Outras cores\nInforme a cor do carro: ");
		scanf("%d",&cor);
		printf("\nInforme a placa do carro\n");
		scanf("%s",placa);
		if(modelo == 1){
			contFP += 1;
		}
		if(ano < 2010){
			cont10 += 1;
		}
		if(cor == 1){
			contCV += 1;
		}
		for(i=0;i<7;i++){
			if(placa[i] == '5'){
				cont5 += 1;
				i = 6;
			}
		}
		n += 1;
	}
	percentverde = (contCV*100)/controle;
	percentfp = (contFP*100)/ controle;
	percent98 = (cont10*100)/controle;
	percent5 = (cont5*100)/controle;
	printf("\nForam registrados %d carros com a cor verde, equivale a %.2f porcento do total",contCV,percentverde);
	printf("\nForam registrados %d carros com ano de fabricacao antes de 2010, equivale a %.2f porcento do total",cont10,percent98);
	printf("\nForam registrados %d carros Fiat Palio, equivalente a %.2f porcento do total",contFP,percentfp);
	printf("\nPlacas com numero 5: %d//Porcentagem em relacao ao total %.2f",cont5,percent5);
	getch();
	return 0;
}