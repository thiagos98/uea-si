#include <stdio.h>
#include <string.h>
/* Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa e retorna o seu peso ideal. 
Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 x alt - 58 e, para mulheres, peso ideal = 62 * alt - 58 */

float calc_peso(float alt,char sexo[10]);
int main(int argc, char** argv){
	float pesoid=0,altura;
	char sexo[10];
	printf("Informe sua altura em m: ");
	scanf("%f",&altura);
	printf("Informe seu sexo[m-masculino/f-feminino]: ");
	scanf("%s",sexo);
	pesoid = calc_peso(altura,sexo);
	printf("O seu peso ideal e %.2fKg",pesoid);
	return 0;
}

float calc_peso(float alt,char sexo[10]){
	float pesoid;
	if(strcmp(sexo,"m")==0){
		pesoid = 72.7*alt - 58;
	}
	else if (strcmp(sexo,"f")==0){
		pesoid = 62*alt - 58;
	}
	return pesoid;
}