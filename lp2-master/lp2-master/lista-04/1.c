#include <stdio.h>
#include <math.h>

void volume(int r){
    float PI,v;
    PI=3.14;
    v=4/3*PI*(pow(r,3));
    printf("O volume da esfera de raio %d e %.2f",r,v);
    
}



int main(){
    int raio;
    printf("Informe o raio da esfera:");
    scanf("%d",&raio);
    volume(raio);
    return 0;
}
