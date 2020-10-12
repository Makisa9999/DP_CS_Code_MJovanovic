#include <stdio.h>
#include <stdlib.h>

int main()
{
    while (1) {
        char Result;
        int Male, Female = 0;
        time_t rawtime;
        struct tm * timeinfo;

        int x = 0;
        printf("THIS PROGRAM IS ABOUT COUNTING PEOPLE!\n");
        do {

            printf("\nMale ('M')\nFemale ('F')\n");
            Male, Female;

            scanf(" %c", &Result);
            switch (Result) {
            case 'M':
                Male = Male + 1;
                printf(" Male: %d Female: %d \n", Male, Female);
                time ( &rawtime );
                timeinfo = localtime ( &rawtime );
                printf ( "Current local time and date: %s", asctime (timeinfo) );
                break;
            case 'm':
                Male = Male + 1;
                printf(" Male: %d Female: %d \n", Male, Female);
                time ( &rawtime );
                timeinfo = localtime ( &rawtime );
                printf ( "Current local time and date: %s", asctime (timeinfo) );
                break;

            case 'F':
                Female = Female + 1;
                printf(" Male: %d Female: %d \n", Male, Female);
                time ( &rawtime );
                timeinfo = localtime ( &rawtime );
                printf ( "Current local time and date: %s", asctime (timeinfo) );
                break;
            case 'f':
                Female = Female + 1;
                printf(" Male: %d Female: %d \n", Male, Female);
                time ( &rawtime );
                timeinfo = localtime ( &rawtime );
                printf ( "Current local time and date: %s", asctime (timeinfo) );
                break;
            default:
                printf("Invalid input!\n");
                time ( &rawtime );
                timeinfo = localtime ( &rawtime );
                printf ( "Current local time and date: %s", asctime (timeinfo) );
                break;
            }
        } while (1);


    }


    return 0;
}
