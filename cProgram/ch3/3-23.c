#include<stdio.h>
void main()
{
    int a,b,c,min;
    printf("input a,b,c :");
    scanf("%d%d%d",&a,&b,&c);
    if(a<b)
        min = a;
    else
        min=b;
    if(c<min)
        min=c;
    printf("The result is : %d\n", min);
}
