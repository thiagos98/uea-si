/*Fazer um algoritmo que calcule  escreva o valor de S onde:*/

#include <stdio.h>
#include <conio.h>
#include <math.h>
int main(int argc, char** argv){
	float numquad,s = 0.0;
	int num = 0;
	int cont = 0;
	while(cont < 10){
		num = num + 1.0;
		numquad = pow(num,2.0);
		if(num%2 == 0){
			s -= num/numquad;
		}
		else{
			s += num/numquad;
		}
		cont += 1;
	}
	printf("%.2f",s);
	getch();
	return 0;
}