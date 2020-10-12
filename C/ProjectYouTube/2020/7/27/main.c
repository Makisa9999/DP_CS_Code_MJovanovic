#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a;
    int b;
    int choice;
    printf("***************Welcome*****************\n");
    printf("Choose what you want to do:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n");
    scanf("%d", &choice);
    printf("Number 1:");
    scanf("%d", &a);
    printf("Number 2:");
    scanf("%d", &b);

    switch (choice)
    {
    case 1:
        printf("%d + %d = %d", a, b, a+b);
        break;
    case 2:
        printf("%d - %d = %d", a, b, a-b);
        break;
    case 3:
        printf("%d * %d = %d", a, b, a*b);
        break;
    case 4:
        printf("%d / %d = %d", a, b, a/b);
        break;

    }
    return 0;
}
