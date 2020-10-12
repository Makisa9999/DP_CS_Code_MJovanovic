#include <stdio.h>
#include <stdlib.h>

int main()
{
        char myName[20];
        int myAge;
    printf("Dobrodosao u moj program napisan u C jeziku.\n");
    printf("Kako se zoves?");
    scanf("%s", myName);
    printf("Koliko imas godina?");
    scanf("%d", &myAge);
    printf("Ti se zoves %s, imas %d godina.\n", myName, myAge);
    printf("%s \t\t\t\t\t\t\t %d\n", myName, myAge);
    return 0;
}
