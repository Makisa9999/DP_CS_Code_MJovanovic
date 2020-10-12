#include <stdio.h>
#include <stdlib.h>

int main()
{
    int age;
    char gender;

    printf("Enter Your Age: ");
    scanf(" %d", &age);
    // %c je da ti program trazi odredjen karakter
    printf("What is your gender? (m/f)");
    scanf(" %c", &gender);

    if (age >= 18) {
        printf("You may proceed to the webpage!\n");
        if (gender == 'm') {printf("Welcome big guy!\n");}
        if (gender == 'f') {printf("Welcome girl!\n");}
    }
    if (age < 18) {
        printf("Nothing to see here!");
    }
    return 0;
}
