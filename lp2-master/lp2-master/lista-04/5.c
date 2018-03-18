#include <stdio.h>

void converte(int duracao)
{
    float min,hora;
    min=duracao/60;
    hora=duracao/3600;
    printf("\nO Tempo convertido em minutos e:%.2f min:",min);
    printf("\nO Tempo convertido em horas e:%.2f hr:",hora);
    printf("\nO Tempo em segundos e:%.2f seg:",duracao);
	return 0;
}


int main(int argc, char** argv){
    int tempo;
    printf("Digite o tempo de duracao da fabrica em segundos:");
    scanf("%d",&tempo);
    converte(tempo);
	return 0;
}
