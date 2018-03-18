/*Escreva uma função recursiva eficiente que receba inteiros positivos 
	k e n e calcule kn*/
	
#include <stdio.h>

int pot(int base,int exp){
	if(base == 0){
		return 0;
	} else if(exp == 0){
		return 1;
	} else if(exp == 1){
		return base;
	} else{
		return base * pot(base,exp - 1);
	}
}

int main(int argc, char** argv){
	int base,exp,res=0;
	printf("Base e Exp: ");
	scanf("%d %d",&base,&exp);
	res = pot(base,exp);
	printf("\n%d",res);
	return 0;
}