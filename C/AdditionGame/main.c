#include <stdio.h>
#include <stdlib.h>

int main()
{
    int answerOne;
    int answerTwo;
    int answerThree;
    int answerFour;
    int answerFive;
    printf("Hello world!\n");
    printf("*********************************************************WELCOME********************************************************\n");
    printf("This is my program for learning maths addition to 10.\nLets begin with first question.\n");
    printf("You will have 3 chances to get every question right.\n");
    printf("What's 1+5=?\n");
    scanf("%d", &answerOne);
    if (answerOne == 6) {
        printf("Goodjob! Proceed to the next question.\n");
    } else {
        printf("WRONG! Try Again!\n");
        printf("What's 1+5=?\n");
        scanf("%d", &answerOne);
        if (answerOne == 6) {
        printf("Goodjob! Proceed to the next question.\n");
        } else {
        printf("WRONG! Try Again!\n");
        printf("What's 1+5=?\n");
        scanf("%d", &answerOne);
        if (answerOne == 6) {
        printf("Goodjob! You got a little lucky!\n");
        } else {
        printf("WRONG! Maths is not for you! But, try another example!\n");
        }
        }
        }

    printf("What's 5+5=?\n");
    scanf("%d", &answerTwo);
    if (answerTwo == 10) {
        printf("Goodjob! Proceed to the next question.\n");
    } else {
        printf("WRONG! Try Again!\n");
        printf("What's 5+5=?\n");
        scanf("%d", &answerTwo);
        if (answerTwo == 10) {
            printf("Goodjob! Proceed to the next question.\n");
        } else {
            printf("WRONG! Try Again!\n");
            printf("What's 5+5=?\n");
            scanf("%d", &answerTwo);
            if (answerTwo == 10) {
                printf("You got lucky! You may proceed to the next question.\n");
        } else {
                printf("Maybe Maths is not for you! Try another example.\n");
        }
        }
        }

        printf("What's 1+3=?\n");
        scanf("%d", &answerThree);
        if (answerThree == 4) {
            printf("Goodjob! Proceed to the next question.\n");
        } else {
            printf("WRONG! Try Again!\n");
            printf("What's 1+3=?\n");
            scanf("%d", &answerThree);
            if (answerThree == 4) {
                printf("Goodjob! Proceed to the next question.\n");
            } else {
                printf("WRONG! One more try!\n");
                printf("What's 1+3=?\n");
                scanf("%d", &answerThree);
                if (answerThree == 4) {
                    printf("Last try! Got a little lucky!\n");
                } else {
                    printf("Maybe maths is not for you! But, try another example.\n");
                }
            }
        }
        printf("What's 6+3=?\n");
        scanf("%d", &answerFour);
        if (answerFour == 9) {
            printf("Goodjob! Proceed to the next question.\n");
        } else {
            printf("WRONG! Try Again!\n");
            printf("What's 6+3=?\n");
            scanf("%d", &answerFour);
            if (answerFour == 9) {
                printf("Goodjob! Proceed to the next question.\n");
            } else {
                printf("WRONG! One more try!\n");
                printf("What's 6+3=?\n");
                scanf("%d", &answerFour);
                if (answerFour == 9) {
                    printf("Last try! Got a little lucky!\n");
                } else {
                    printf("Maybe maths is not for you! But try another one.\n");
                }
            }
        }
    printf("What's 1+7=?\n");
        scanf("%d", &answerFive);
        if (answerFive == 8) {
            printf("Goodjob! Proceed to the next question.\n");
        } else {
            printf("WRONG! Try Again!\n");
            printf("What's 1+7=?\n");
            scanf("%d", &answerFive);
            if (answerFive == 8) {
                printf("Goodjob! Proceed to the next question.\n");
            } else {
                printf("WRONG! One more try!\n");
                printf("What's 1+7=?\n");
                scanf("%d", &answerFive);
                if (answerFive == 8) {
                    printf("Last try! Got a little lucky!\n");
                } else {
                    printf("Maybe maths is not for you!\n");
                }
            }
        }
    return 0;
}
