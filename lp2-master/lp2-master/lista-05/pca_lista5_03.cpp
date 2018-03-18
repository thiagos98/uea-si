#include <stdio.h>
#define tamanho 4
#define limite 20

char nome[tamanho][limite], profissao[tamanho][limite];

int cadastro(int T)
{
    int i;
    for(i = 0; i < T; i++){
        printf("Qual o seu nome? \n");
        scanf("%s", &nome[i]);
        printf("Qual o seu emprego? \n");
        scanf("%s", &profissao[i]);
        printf("\n");
    }
}

int imprimir_cadastro(int T)
{
    int i;
    for(i = 0; i < T; i++){
        printf("=> %s eh %s \n", nome[i], profissao[i]);
    }
}

int main()
{
    cadastro(tamanho);
    imprimir_cadastro(tamanho);

    return 0;
}
