#include "stdio.h"
void main()

{
int *p1, *p2, a,b,t;
printf("input a and b:");
scanf("%d,%d",&a,&b);
p1=&a; p2=&b;
if(*p1<*p2)
    {t=*p1;*p1=*p2;*p2=t;}
printf("a=%d,b=%d\n",*p1,*p2);
}
