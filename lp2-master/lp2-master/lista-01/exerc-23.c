/*23.	Uma pessoa resolveu fazer uma aplicação em uma poupança programada. Para calcular seu rendimento, 
ela deverá fornecer o valor constante da aplicação mensal, a taxa e o número de meses. 
Sabendo-se que a fórmula usada para este cálculo é:
Valor acumulado = P * (1+i)n -1/i                     i=taxa; P=aplicação; n=número de meses
*/

#include<stdio.h>
#include<math.h>

int main(int argc, char** argv)
{
	int deposito,meses;
	float taxa,valoracumulado;
	
	printf("Informe o valor do deposito: R$");
	scanf("%d",&deposito);
	printf("Informe a taxa de juros(valor decimal): ");
	scanf("%f",&taxa);
	printf("Informe a quantidade de meses: ");
	scanf("%d",&meses);
	
	valoracumulado = (deposito * pow((1 + taxa),meses)) - (1 / taxa);
	
	printf("O valor acumulado foi R$%.2f",valoracumulado);
	return 0;
}