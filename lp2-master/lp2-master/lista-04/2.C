#include <stdio.h>
#include <string.h>
#include <math.h>

int media(int nota1 , int nota2 , int nota3 , char letra[10]);

int main()
{
    printf("\n----------------------------------------------------------------------");
    printf("\n MÉDIA - P -(PARA PONDERADA) - A - (PARA ARITMETICA) H-(PARA HARMONICA)");
    printf("\n----------------------------------------------------------------------");

    char letra[10];
    float n1,n2,n3,med;

    printf("\n--------------------------");
	printf("\nDigite a primeira nota: ");
	scanf("%f",&n1);
	printf("\nDigite a segunda nota: ");
	scanf("%f",&n2);
	printf("\nDigite a terceira nota: ");
	scanf("%f",&n3);
	printf("Informe o tipo de media: ");
	scanf("%s",letra);
	med = media(n1,n2,n3,letra);
	printf("A media do aulo foi %.2f",med);
	return 0;
}

int media(int nota1 , int nota2 , int nota3 , char letra[10])
{
    float mp,ma,mh;
	if(strcmp(letra,"p")==0){
		mp=(nota1*5+nota2*3+nota3*2)/10;
		return mp;
	}
	if (strcmp(letra,"a")==0){
		ma=(nota1+nota2+nota3)/3;
		return ma;
	}
    if(strcmp(letra,"h")==0){
		mh=(3/((1/nota1)+(1/nota2)+(1/nota3)));
		return mh;
	}
	return 0;
}





