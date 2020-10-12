#include <stdio.h>
#include <stdlib.h>

int main()
{
    int userAge;
    int currentYear;
    char hadBirthday[3];
    currentYear = 2020;
    printf("Hello and welcome!\nWhat is your age? \n");
    scanf("%d", &userAge);
    printf("Did you have a birthday this year? (Y/N)");
    scanf("%s", hadBirthday);
    if (hadBirthday == 'Y') {
        userAge + 1;
    }
    if (hadBirthday == 'N') {
        userAge + 0;
    }
    printf("So your birth year is %d", currentYear - userAge);

    return 0;
}
