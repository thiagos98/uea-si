#include <stdio.h>
#include <stdlib.h>
#define tam 50

void push(int i);
int pop();

int *topo,*p1,pilha[tam];

int main(int argc, char** argv)
{
	int valor;
	topo = pilha;
	p1 = pilha;
	do {
		printf("\nDigite um valor: ");
		printf("\n (0) para remover elemento da pilha\n(-1) para encerrar\n qualquer outro");
		scanf("%d",&valor);
		if(valor != 0){
			push(valor);
		} else {
			printf("\nValor do topo é %d \n\n\n",pop());
		}
	} while (valor != -1);
	return 0;
}

void push(int i){
	p1++;
	if(p1 == (topo + tam)){
		printf("Pilha cheia. Impossível inserir elemento \n");
		exit(0);
	}
	
	*p1 = i;
}

pop(){
	if(p1 == topo){
		printf("Pilha vazia\n");
	} else {
		printf("Elementos sera removido \n");
	}
	
	p1--;
	return *(p1+1);
}









