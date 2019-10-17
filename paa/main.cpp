//
// Created by thiagosb on 16/10/2019.
//
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define N 200500
#define M 100005
#define maxn 205
#define MOD 1000000000000000007
int n,len[2];
char str[2][N];
bool equalstr(char st1[],char st2[],int s1,int e1,int s2){
    for(int i = s1;i<=e1;i++){
        if(st1[i] != st2[s2++]) return false;
    }
    return true;
}
bool Check(char str1[],char str2[],int s1,int e1,int s2,int e2){
    //printf("%d %d %d %d\n",s1,e1,s2,e2);
    int l = (e1 - s1 + 1);
    if(l & 1){
        return equalstr(str1,str2,s1,e1,s2);
    }
    else {
        int mid = l / 2;
        if(   Check(str1,str2,s1,s1 + mid - 1,s2,s2 + mid - 1)
           && Check(str1,str2,s1 + mid,e1,s2 + mid ,e2)) return true;
        if(   Check(str1,str2,s1,s1 + mid - 1,s2 + mid ,e2)
           && Check(str1,str2,s1 + mid,e1,s2,s2 + mid - 1)) return true;
    }
    return false;
}
int main()
{
    while(SS(str[0])!=EOF)
    {
        SS(str[1]);
        len[0] = strlen(str[0]);
        len[1] = strlen(str[1]);
        if(Check(str[0],str[1],0,len[0] - 1,0,len[1] - 1)){
            printf("YES\n");
        }
        else
            printf("NO\n");
    }
    return 0;
}