#include <stdio.h>
#include <stdlib.h>

int main()
{
    char firstName[15];
    char lastName[15];
    int birthYear;
    int currentYear = 2020;
    int choice;
    int withBirthday =(2020-birthYear);
    int noBirthday =(2020-birthYear)-1;
    printf("************************WELCOME************************\n");
    printf("This is my program!\n");
    printf("Please enter your first name:\n");
    scanf("%s", firstName);
    printf("Please enter your last name:\n");
    scanf("%s", lastName);
    printf("What is your birth year?\n");
    scanf("%d", &birthYear);
    printf("Did you celebrate your birthday this year?\n1.Yes\n2.No\n");
    scanf("%d", &choice);
    printf("Your birth year is: %d\n", birthYear);
    printf("If you celebrated you birthday you would be %d years old.\n", withBirthday);
    printf("if you did not celebrate your birthday you are %d years old.\n", noBirthday);
    switch (choice)
    {
        case 1:
            printf("That means that your are %d years old.\n", withBirthday);
            printf("Your name is %s %s and you are %d years old!\n", firstName, lastName, withBirthday);
            break;
        case 2:
            printf("That means that you are %d years old.\n", noBirthday);
            printf("Your name is %s %s and you are %d years old!\n", firstName, lastName, noBirthday);
            break;
    }


    return 0;
}
