#include <stdio.h>
#include <stdlib.h>
#include "Mario.h"

int main()
{
    printf("Name: %s\t\t\t\t\t", MYNAME);
    printf("Age: %d\n\n", MYAGE);
    int weight = 180;
    printf("If I ate a twelve pound watermelon, I would weight %d lbs! \n", weight+12);

    int a = 75;
    int b = 22;
    float c = a;
    float d = b;
    printf("%d\n", a/b);
    printf("%f\n", c/d);
    return 0;
}
