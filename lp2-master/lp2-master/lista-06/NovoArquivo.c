#include <stdio.h>

int main(int argc, char** argv)
{
	int x=10;
	int *p1,*p2;
	
	p1 = &x;
	p2 = p1;
	
	printf("%p  \n",p1);
	printf("%p  ",p2);
	return 0;
}