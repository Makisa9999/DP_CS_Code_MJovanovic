#include <stdio.h>
#include <stdlib.h>
#include "MariosInfo.h"


int main()
{
        printf("Hello world!\n");
        printf("Mario And Iko Are Programmers!\n");
        printf("We are awesome.\n");
        printf("Djosa is cool!\n");
        printf("We are listening to music!\n");
        printf("Are we going home!\n");
        printf("We are cool kids\n");
        printf("I am going to the park tomorrow\a\n");
        printf("Today is a sunny day.\t");
        printf("Today will be a hot day.\n");

        int age1;
        age1 = 15;
        printf("Mario is %d years old!\n", age1);

        int number;
        number = 98239-93285;
        printf("This is mathematical operation %d!\n", number);

        int dadsAge;
        int dadsBirthYear;
        int currentYear;

        dadsBirthYear = 1963;
        currentYear = 2018;
        dadsAge = currentYear - dadsBirthYear;

        printf("My dad is %d years old!\n", dadsAge);

        char name [16] = "Mario Jovanovic";
        printf("My name is %s.\n", name);

        name [2] = 'k';
        printf("My name is %s.\n", name);
        name [2] = 'r';
        printf("His name is also %s.\n", name);

        char food[] = "tuna";
        printf("I love %s.\n", food);

        strcpy(food, "eggs");
        printf("I love %s.\n", food);

        int girlsAge = (AGE / 2) + 7;
        printf("%s can date girls %d or older.\n", MYNAME, girlsAge);

        char firstName [20];
        char crush [20];
        int numberOfHouses;

        printf("What is your name?\n");
        scanf("%s", firstName);
        printf("What is yours crush name?\n");
        scanf("%s", crush);
        printf("How many houses will you have?\n");
        scanf("%d", &numberOfHouses);
        printf("Your name is %s. Yours crush name is %s. You will Have %d houses.\n", firstName, crush, numberOfHouses);

        int a;
        int b;
        a = 86;
        b = 22;
        printf("%d \n", a/b);

        float c;
        float d;
        c = 86;
        d = 22;
        printf("%f \n", c/d);

    return 0;
}
