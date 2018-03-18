/*Construa um algoritmo que leia as informações de: horas trabalhadas (HT), valor da hora trabalhada (VH). 
Calcule e apresente o salário líquido do empregado, baseado nas tabelas abaixo.  
OBS: Salário Líquido = Salário Bruto – INSS – 
Imposto de Renda Salário Bruto = Horas trabalhadas * Valor da hora trabalhada INSS = 11% do salário bruto Imposto de Renda  
após descontar o INSS usar esse valor e ler a alíquota do imposto de renda e parcela a deduzir na tabela abaixo 
Salário Bruto – INSS Alíquota Valor a Deduzir 
Até $1.257,12 /Isento (0%)  
De $1.257,13 até $2.512,08/ 15%/ $188,57 
Mais que $2.512,08/ 27,5%/ $502,58 
 
OBS: Imposto de Renda = Alíquota * (Salário Bruto – INSS) – Valor a Deduzir 
 */

#include <stdio.h>

int main(int argc, char** argv)
{
	float htrabalhadas,valorhtrab,salbruto,saliquido,inss,imposto,aliquota,valordeduzir;
	printf("Informe a quantidade de horas trabalhadas: ");
	scanf("%f",&htrabalhadas);
	printf("Informe o valor da hora trabalhada: $");
	scanf("%f",&valorhtrab);
	salbruto = htrabalhadas*valorhtrab;
	inss = 0.11*salbruto;
	if (salbruto - inss < 1257.13)
	{
		aliquota = 0.0;
		valordeduzir = 0;
	}
	else if ((salbruto - inss > 1257.12) && (salbruto - inss < 2512.09))
	{
		aliquota = 0.15;
		valordeduzir = 188.57;
	}
	else if (salbruto - inss > 2512.08)
	{
		aliquota = 0.275;
		valordeduzir = 502.58;
	}
	imposto = aliquota * (salbruto - inss) - valordeduzir;
	saliquido = salbruto - inss - imposto;
	
	printf("Salario Bruto: $%.2f",salbruto);
	printf("\nO salario liquido do funcionario apos os descontos e $%.2f",saliquido);
	return 0;
}