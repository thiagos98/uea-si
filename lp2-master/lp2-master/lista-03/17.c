#include <stdio.h>
#include <conio.h>
#include <math.h>

int main(int argc, char** argv)
{
	float x,aux,s,p;
	int n,i;
	i = 25;
	n = 1;
	s = 0;
	aux = 1;
	scanf("%f",&x);
	while(n <= 25){
		p = pow(x,i);
		p = p/n;
		if (aux > 0){
			s = s + p;
			aux = -1;
		}
		else{
			s = s - p;
			aux = 1;
		}
		n += 1;
		i -= 1;
	}
	printf("O valor do somatorio para X = %.2f e: %.2f",x,s);
	getch();
	return 0;
}