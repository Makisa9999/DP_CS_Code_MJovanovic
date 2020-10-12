#include <stdio.h>
#include <stdlib.h>

int main()
{
    char answer;

    printf("Welcome to my program where I will use or command.\n");
    printf("Do you like hotdog? (y/n) \n");
    scanf(" %c", &answer);
    // ovde mora jedan od testova da bude tacan da bi runovao program

    if ( (answer == 'y') || (answer == 'n')) {
        printf("Your answer is correct.\n");
    } else {
        printf("Invalid entry!\n");
    }

    return 0;
}
