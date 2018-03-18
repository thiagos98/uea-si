/*Foi realizada uma pesquisa em Porto Alegre, com um número desconhecido de pessoas.     De cada entrevistado foram colhidos os seguintes dados:     
a) clube de preferência (1-Grêmio; 2-Internacional; 3-Outros);     
b) salário;    
c) cidade de origem (0-Porto Alegre; 1-Outras).   
Deseja-se saber: 
a) número de torcedores por clube; 
b) média salarial dos torcedores do Grêmio e do Internacional; 
c) número de pessoas nascidas em Porto Alegre que não torcem por nenhum dos dois primeiros clubes; 
d) número de pessoas entrevistadas. */

#include <stdio.h>
#include <conio.h>

int main(int argc, char** argv)
{
	int contG=0,contI=0,contOT=0,contPA=0,contOC=0,contPANGI=0,cont=1,aux = 0,opcao,clube,cidade;
	float salario,acmG=0,acmI=0,media=0;
	while(cont){
		printf("\n\n1-Gremio\n2-Internacional\n3-Outros\nClube de Preferencia: ");
		scanf("%d",&clube);
		printf("0-Porto Alegre\n1-Outras\nCidade de Origem: ");
		scanf("%d",&cidade);
		printf("Salario: R$");
		scanf("%f",&salario);
		if(clube == 1){
			contG += 1;
			acmG += salario;
		}
		else if(clube == 2){
			contI += 1;
			acmI += salario;
		}
		else if(clube == 3){
			contOT += 1;
		}
		else{
			printf("Informe uma opcao valida");
		}
		if(cidade == 0){
			contPA += 1;
		}
		else if (cidade == 1){
			contOC += 1;
		}
		if(cidade == 0 && clube == 3){
			contPANGI += 1;
		}
		cont += 1;
		printf("Digite -1 para sair: ");
		scanf("%d",&opcao);
		if(opcao == -1){
			aux = cont;
			cont = 0;
		}
	}
	media = (acmG+acmI)/(contG+contI);
	printf("Torcedores do Gremio: %d\nTorcedores do Internacional: %d\nTorcedores de outros times: %d",contG,contI,contOT);
	printf("\nMoradores de Porto Alegre: %d\nMoradores de outras cidades: %d",contPA,contOC);
	printf("\nMedia salario entre os torcedores do Gremio e do Internacional: R$%.2f",media);
	printf("\nNumero de pessoas nascidas em Porto Alegre que torcem para outros times: %d",contPANGI);
	printf("\nNumero de pessoas entrevistadas: %d",cont);
	getch();
	return 0;
}