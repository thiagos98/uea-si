#include <stdio.h>

int main(int argc, char** argv)
{
	float htrabalhadas,valorhtrab,salbruto,saliquido,inss,imposto,aliquota,valordeduzir;
	printf("Informe a quantidade de horas trabalhadas: ");
	scanf("%f",&htrabalhadas);
	printf("Informe o valor da hora trabalhada: $");
	scanf("%f",&valorhtrab);
	salbruto = htrabalhadas*valorhtrab;
	if (salbruto < 800.46)
	{
		inss = salbruto * 0.0765;
	}
	else if (salbruto > 800.45 && salbruto < 900.01)
	{
		inss = salbruto*0.0865;
	}
	else if (salbruto > 900 && salbruto < 1334.08)
	{
		inss = salbruto*0.09;
	}
	else if (salbruto > 1334.07 && salbruto < 2668.16)
	{
		inss = salbruto*0.11;
	}
	else
	{
		inss = 315.5;
	}
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