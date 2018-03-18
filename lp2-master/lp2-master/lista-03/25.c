/*Escrever um programa para gerar e escrever uma tabela com os valores de seno de um Angulo A em radianos, 
utilizando a série de Mac-Laurin Truncada apresentada a seguir
Condições: os valores dos ângulos devem variar de 0.0 a 6.3, inclusive, de 0.1 em 0.1 */
// radianos = graus * PI / 180; 
#include <stdio.h>
#include <conio.h>
#include <math.h>

int main(int argc, char** argv){
	float cont = 0.1;
	float senoA=0.0;
	while(cont < 6.4){
		senoA = cont - (pow(cont,3.0)/6.0) + (pow(cont,5.0)/120.0) - (pow(cont,7.0)/5040.0);
		printf("\n	%.2f",senoA);
		cont += 0.1;
	}
	return 0;
}