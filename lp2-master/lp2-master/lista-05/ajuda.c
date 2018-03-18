#include <stdio.h>

#define tamanho 10

int fperfeitos(int numero);
int verificar_perfeitos(int pares[], int cont_par);
int fprimos(int numero);
int verificar_primos(int impares[], int cont_impar);
int separar(int vetor[], int pares[], int impares[], int *cont_par, int *cont_impar);
int escrever_vetor(int vetor[], int T, char *texto);
void ler_vetor(int vetor[]);

int main()
{
    int vetor[tamanho], pares[tamanho], impares[tamanho], tPar, tImpar;
    ler_vetor(vetor);
    escrever_vetor(vetor, tamanho, "vetor lido");
    separar(vetor, pares, impares, &tPar, &tImpar);
    escrever_vetor(pares, tPar,"vetor par");
    escrever_vetor(impares, tImpar, "vetor impar");
    printf("O total de primos impares eh %d \n",verificar_primos(impares, tImpar));
    printf("O total de perfeitos pares eh %d \n",verificar_perfeitos(pares, tPar));
    return 0;
}

void ler_vetor(int vetor[])
{
    int i;
    for(i = 0; i < tamanho; i++){
        printf("vetor[%d] = : ", i+1);
        scanf("%d", &vetor[i]);
    }
}
int escrever_vetor(int vetor[], int T, char *texto)
{
    int i;
    for(i = 0; i < T; i++){
        printf("%s[%d] = %d \n", texto, i+1, vetor[i]);
    }
    printf("\n\n");
}

int separar(int vetor[], int pares[], int impares[], int *cont_par, int *cont_impar)
{
    int i;
    *cont_par = 0;
    *cont_impar = 0;

    for(i = 0; i < tamanho; i ++){
        if(vetor[i] % 2 == 0){
            pares[*cont_par] = vetor[i];
            *cont_par = *cont_par + 1;
        }else{
            impares[*cont_impar] = vetor[i];
            *cont_impar = *cont_impar + 1;
        }
    }
}

int verificar_primos(int impares[], int T)
{
    int i, cont_primo = 0;;
    for(i = 0; i < T; i++){
        if (fprimos(impares[i]) == 2)
            cont_primo = cont_primo + 1;
    }
    return cont_primo;
}

int fprimos(int numero)
{
    int i, contador = 0;
    for(i = 1; i <= numero; i++){
        if(numero % i == 0){
            contador = contador + 1;
        }
    }
    return contador;
}

int verificar_perfeitos(int pares[], int cont_par)
{
    int i, cont_perfeitos=0;
    for(i = 0; i < cont_par; i++){
        if (fperfeitos(pares[i]) == pares[i])
            cont_perfeitos = cont_perfeitos + 1;
    }
    return cont_perfeitos;
}


int fperfeitos(int numero)
{
    int i, contador = 0;
    for(i = 1; i < numero; i++){
        if(numero % i == 0){
           contador = contador + i;
        }
    }

        return contador;
}