#include <stdio.h>
#include <stdlib.h>

int main()
{
    int number;
    printf("******************WELCOME*********************\n");
    printf("Select a number(1-infinity):");
    scanf("%d", &number);

    switch (number)
    {
    default:
        printf("BORING %d", number);
        break;

    case 69:
        printf("NICE %d", number);
        break;
    }
    return 0;
}
