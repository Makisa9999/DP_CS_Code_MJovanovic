#include <stdio.h>
#include <stdlib.h>

int main()
{
    char myName[20];
    char mySurname[20];
    char customersFeelings[20];
    char answerQuestion[20];
    char newFeelings[20];

    printf("What is your name? \n");
    scanf("%s", myName);

    printf("What is your surname? \n");
    scanf("%s", mySurname);

    printf("Welcome: %s %s \n", myName, mySurname);

    printf("How are you doing today? \n");
    scanf("%s", customersFeelings);

    printf("Since you are doing %s I will try to make you laugh. \n", customersFeelings);
    printf("Why did the chicken cross the road? \n");

    scanf("%s", answerQuestion);
    printf("To get to the other side. \n");
    printf("Did I make you laugh? \n");
    scanf("%s", newFeelings);
    printf(":)");
    return 0;
}
