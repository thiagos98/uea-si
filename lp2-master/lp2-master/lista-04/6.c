
int converte(int meses,int anos,int dias)
{
    float total_idade=0;
    meses=meses*30.41;
    anos=anos*365;
    total_idade=(meses+anos+dias);
    printf("%.2f",total_idade);


}


int main()
{
    int an,dias,ms;
    printf("Digite a sua idade em anos:");
    scanf("%d",&an);
    printf("Digite a sua idade em meses:");
    scanf("%d",&ms);
    printf("Digite a sua idade em dias:");
    scanf("%d",&dias);
    converte(an,ms,dias);
}
