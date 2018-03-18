#include <stdio.h>

/*def pot(base,exp):
	if base == 0:
		return 0
	elif exp == 0:
		return 1
	elif exp == 1:
		return base
	elif exp > 1:
		return base * pot(base,exp - 1)

base = int(input("Base: "))
exp = int(input("Expoente: "))

potencia = pot(base,exp)                   
print(potencia)
*/

int pot(int base,int exp);
int main(int argc, char** argv)
{
	int base,exp,potencia;
	printf("Informe a base e o expoente: ");
	scanf("%d %d",&base,&exp);
	potencia = pot(base,exp);
	printf("Potencia: %d",potencia);
	return 0;
}

int pot(int base,int exp){
	if(base == 0){
		return 0;
	}
	else if(exp == 0){
		return 1;
	}
	else if(exp == 1){
		return base;
	}
	else if(exp > 1){
		return base * pot(base,(exp-1));
	}
}