#include <stdio.h>
#include <stdlib.h>
#include "Mario.h"

int main()
{
    char CustomerName[20];
    int CustomerAge;

    printf("Name: %s\t\t\t\t\t\t", MYNAME);
    printf("Age: %d\n", MYAGE);

    printf("What is your name?\n");
    scanf("%s", CustomerName);

    printf("What is your age?\n");
    scanf("%d", &CustomerAge);

    printf("%s, welcome to my first program. I hope you like it as much as I do. This Program is about saving your name(%s),\n and your age(%d).\n", CustomerName, CustomerName, CustomerAge);

    return 0;
}
