#include <stdio.h>
#include <stdlib.h>

int main()
{
    int kidsBeatUp;
    int hoursStudied;

    printf("************************************WELCOME************************************\n");
    printf("How many kids did you beat up this week?\n");
    scanf(" %d", &kidsBeatUp);

    printf("How many hours did you study this week?\n");
    scanf(" %d", &hoursStudied);

    // Mozes da dodajes koliko oces testova

    if( (kidsBeatUp == 0) && (hoursStudied >= 20) ) {
        printf("You are a good student!\n");
    } else {
        printf("You are a bad student!\n");
    }
    return 0;
}
