#include <stdio.h>
#include <stdlib.h>


int main()
{
    while (1) {
        int Result;
        int Male, Female;
        int x = 0;
        char datap[1000];
        do {
        printf("M start: %d\n", Male);
        printf("THIS PROGRAM IS ABOUT COUNTING PEOPLE!\n");
        printf("1. Male\n2. Female\n");
        scanf(" %d", &Result);
        switch (Result) {
            case 1:
                printf("M: %d; F: %d;\n", Male + 1, Female);

                break;
            case 2:
                printf("M: %d; F: %d;\n", Male, Female + 1);

                break;
            default:
                printf("Invalid Input\n");
                break;
            }
        } while (x = 1);
        }
    return 0;
    }
