/*28.	Faça um algoritmo que receba, para um aluno, três notas de provas e quatro de trabalhos, 
calcule a média parcial (ponderada) sabendo que o peso das medias das provas representa 70% e a 
média dos trabalhos 30%. O programa calculará também a nota mínima para que o aluno passe na prova 
final, utilizando a fórmula apresentada abaixo. 
Todos os dados devem ser mostrados
final = (50 - media parcial*6)/4*/

#include <stdio.h>

int main(int argc, char** argv)
{
	float ap1,ap2,ap3,at1,at2,at3,at4;
	float mparcial,ppfinal;
	
	printf("Calculo das notas.\nNotas das provas(separe por espaco cada uma):\n");
	scanf("%f %f %f",&ap1,&ap2,&ap3);
	printf("Notas dos trabalhos:\n");
	scanf("%f %f %f %f",&at1,&at2,&at3,&at4);
	
	
	mparcial = ((0.7 * ((ap1+ap2+ap3)/3)) + (0.3 * ((at1+at2+at3+at4)/3)));
	ppfinal = (50 - mparcial*6)/4;
	
	printf("Media parcial: %.1f",mparcial);
	printf("\nFalta para final %.1f pontos",ppfinal);
	printf("\nNota Prova 1: %.1f\nNota Prova 2: %.1f\nNota Prova 3: %.1f",ap1,ap2,ap3);
	printf("\nNota Trabalho 1: %.1f\nNota Trabalho 2: %.1f\nNota Trabalho 3: %.1f\nNota Trabalho 4: %.1f",at1,at2,at3,at4);
	
	return 0;
}