#include <stdio.h>
#include <stdlib.h>

int main()
{
    float grade = 0;
    float scoreEntered = 0;
    float numberOftests = 0;
    float average = 0;

    printf("Press 0 when complete. \n\n");

    do {

        printf("Tests: %.0f\tAverage: %.2f \n",  numberOftests, average);
        printf("\nEnter test score: ");
        scanf("%f", &scoreEntered);
        grade += scoreEntered;
        numberOftests++;
        average = grade / numberOftests;


    } while (scoreEntered != 0);


    return 0;
}
