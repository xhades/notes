#include "stdio.h"
#include "string.h"

void main()
{
    char a[20],b[20];
    strcpy(a, "apple");
    strcpy(b,a);
    strcpy(a,"OK");
    puts(a);
    puts(b);
}

