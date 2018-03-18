#include <stdio.h>

/* Faça um procedimento que lê 50 valores inteiros e imprima o maior e o menor 
deles*/
void verificar(int quant);
int main(int argc, char** argv)
{
	int quant;
	printf("Quantos numeros para serem lidos?\n");
	scanf("%d",&quant);
	verificar(quant);
	return 0;
}

void verificar(int quant){
	int i,numero,maior,menor;
	for(i=0;i<quant;i++){
		printf("%do numero: ",(i+1));
		scanf("%d",&numero);
		if(i==0){
			maior = menor = numero;
		}
		else if(numero > maior){
			maior = numero;
		}
		else if(numero < menor){
			menor = numero;
		}
	}
	printf("Maior: %d\nMenor: %d",maior,menor);
}