#include<stdio.h>
#include<math.h>
#include <conio.h>
//s = 1/1^3 + 1/3^3 + 1/5^3
int main()
{
	float s = 0,i = 0,aux = 1;
	float pi;	
	int den = 1;
	while(i <= 51)
	{
		if (aux > 0)
		{
			s += 1/pow(den,3);
			aux = -1;			
		}
		else 
		{
			s = s - (1/pow((den),3));
			aux = 1;
		}
		den += 2;
		i += 1;
	}	
	pi = cbrt(s*32);
	printf("Pi: %f",pi);
	getch();
	return 0;
}