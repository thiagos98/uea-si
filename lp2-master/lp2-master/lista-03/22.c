/* Uma pesquisa sobre algumas características físicas da população de uma determinada região coletou os seguintes dados, referentes a cada habitante, 
para análise: a) sexo (1-masculino, 2-feminino); 
b) cor dos olhos (1-azuis, 2-verdes, 3-castanhos); 
c) cor dos cabelos (1-louros, 2-castanhos, 3-pretos); 
d) idade em anos. 
 
Para cada habitante foi preenchido um cartão com estes dados e o último cartão, que não corresponde a ninguém, contém o valor de idade igual a -1. 
Fazer um programa que determine e escreva:          
a) a maior idade dos habitantes;            
b) a percentagem de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos,  inclusive, e que tenham olhos verdes e cabelos louros.
Faça um PROGRAMA para calcular:
*/

#include <stdio.h>
#include <conio.h>

int main(int argc, char** argv){
	int contSM=0,contSF=0,contOA=0,contOV=0,contOC=0,contCL=0,contCC=0,contCP=0,contFVL=0,sexo,olhos,cabelo,idade,quantidade,cont = 0,maiorIdade;
	float porcent;
	printf("Quantas pessoas iram participar da pesquisa?\n");
	scanf("%d",&quantidade);
	while(cont<quantidade){
		printf("---Pesquisa---\n1-Masculino\n2-Feminino\nInforme sua sexualidade: ");
		scanf("%d",&sexo);
		printf("\n1-Azuis\n2-Verdes\n3-Castanhos\nInforme a cor dos seus olhos: ");
		scanf("%d",&olhos);
		printf("\n1-Louros\n2-Castanhos\n3-Pretos\nInforme a cor do seu cabelo: ");
		scanf("%d",&cabelo);
		printf("Informe a sua idade: ");
		scanf("%d",&idade);
		if(cont==0){
			maiorIdade=idade;
		}
		else{
			if(idade>maiorIdade){
				maiorIdade = idade;
			}
		}
		switch(sexo){
			case 1:
				contSM += 1;
				break;
			case 2:
				contSF += 1;
				break;
			default:
				break;
		}
		switch(olhos){
			case 1:
				contOA += 1;
				break;
			case 2:
				contOV += 1;
				break;
			case 3:
				contOC += 1;
				break;
			default:
				break;
		}
		switch(cabelo){
			case 1:
				contCL += 1;
				break;
			case 2:
				contCC += 1;
				break;
			case 3:
				contCP += 1;
				break;
			default:
				break;
		}
		if((sexo == 2) && (idade > 17 && idade < 36) && (olhos == 2) && (cabelo == 1)){
			contFVL += 1;
		}
		cont += 1;
	}
	porcent = (float) contFVL/(float) cont;
	porcent = 100*porcent;
	printf("\nA maior idade  e %d",maiorIdade);
	printf("\n\nA porcentagem de  individuos do sexo feminino cuja idade esta entre 18 e 35 anos,  inclusive, e que tenham olhos verdes e cabelos louros e %.2f",porcent);
	getch();
	return 0;
}