#include<stdio.h>

int main()
{
	int maior,menor,num;
	int i;
	for (i = 0;i < 10;i++)
	{
		printf("Informe o numero: ");
		scanf("%d",&num);
		if (i == 0)
		{
			maior = menor = num;		
		}
		else 
		{
			if (maior < num)
			{
				maior = num;
			}
			else if (menor > num)
			{
				menor = num;		
			}
		}
	}
	printf("Maior: %d.\nMenor: %d",maior,menor);
	return 0;
}