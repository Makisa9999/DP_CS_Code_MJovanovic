#include <stdio.h>
#include <stdlib.h>
#include "MariosInfo.h"
// You can make a specific file with extension ".h" and save that in the same file where this main file is and include it and all it will do is paste everything from that file there. You will need
//to put it inside of double quotes.
#define MYNAME "Mario Jovanovic"
// Here you can add constant variables which are different because you cannot change those constant variables. You don't need to use semicolon on the end of a row. You can use this when you know
// that this variable is going to stay at this value trough out the whole program.

int main()
{
    printf("Hello world!\n");
    printf("Ja se zovem Mario Jovanovic!\n");
    printf("Imam 15 godina u Avgustu punim 16!\n");
    printf("Hello world je osnovna komanda.\n");
    printf("printf je komanda koju kompjuter cita i ispisuje sta se nalazi u zagradama pod navodnicima.\n");
    printf("/n je komanda koja kaze kompjuteru da predje u novi red.\n");
    printf("/n komanda ide izmedju navodnika.\n");
    printf("Ja idem u gimnaziju Rudjer Boskovic i volim da programiram i da ucim razlicite jezike za programiranje.\n");
    printf("Mario is awesome. \t \a \n");
    /* \a je alert i zbog toga se cuje onaj zvuk.  */
    // komentar moze i ovako da se zapocne
    printf("%s is the best person in the world.\n", "Mario Jovanovic" );
    printf("%s is the %s %s in the %s!\n", "Mario Jovanovic", "best", "programmer", "world");
    // %s will only change words. %d will change a whole number or an integer. %f is only used for decimal numbers.
    // The number of decimal places that a computer is going to print can be changed by putting for example %.2f. This .2 is going to tell computer to circle the number to two decimal places.
    printf("Number Pi is %.9f.\n", 3.1415926535);
    printf("%s is %d years old.\n", "Mario Jovanovic", 14);
    printf("Pi is %.1f.\n", 3.1415926535);
    printf("Pi is %.2f.\n", 3.1415926535);
    printf("Pi is %.3f.\n", 3.1415926535);
    printf("Pi is %.4f.\n", 3.1415926535);
    printf("Pi is %.5f.\n", 3.1415926535);
    printf("Pi is %.6f.\n", 3.1415926535);
    printf("Pi is %.7f.\n", 3.1415926535);
    printf("Pi is %.8f.\n", 3.1415926535);
    printf("Pi is %.9f.\n", 3.1415926535);
    printf("Pi is %.10f.\n", 3.1415926535);
    int age;
    age = 15;
    printf("I am %d years old.\n", age);\
    /* You will put the name of your variable, after the "int" for a whole number or integer. i named my variable age and stored the value 15 for it. When I want to display that variable I need to
    put %d instead of the word I am trying to change. After the sentence I need to write the name of the variable that you are going to use. You can also store the value of variable with some
    calculations that will computer figure out.  */
    char personalName[16] = "Mario Jovanovec";
    //                       012345678901234
    //
    printf("I love %s.\n", personalName);
    personalName[13] = 'i';
    printf("I love %s.\n", personalName);
    char personalBestFood [8] = "Hot Dog";
    printf("I love %s.\n", personalBestFood);
    personalBestFood [0] = 'B';
    personalBestFood [1] = 'u';
    personalBestFood [2] = 'r';
    personalBestFood [3] = 'r';
    personalBestFood [4] = 'i';
    personalBestFood [5] = 't';
    personalBestFood [6] = 'o';
    // This above will change the name of letters in the char personalBestFood.
    printf("I live for %s.\n", personalBestFood);
    strcpy(personalBestFood, "Cookie");
    printf("I live for %s.\n", personalBestFood);
    printf("My name is %s", MYNAME);
    int girlsAge = (PERSONALAGE / 2) + 7;
    printf("\n%s can date girls %d or older. \n", PERSONALNAME, girlsAge);
    char yourName[20];
    char yourCrushesName[20];
    int numberOfBabies;
    printf("Write your name.\n");
    scanf("%s", yourName);
    printf("Write your crushes name.\n");
    scanf("%s", yourCrushesName);
    printf("Write how many babies you want.\n");
    scanf("%d", &numberOfBabies);
    // it is important to write "&" sign before an int function right above this comment.
    printf("%s and %s are going to get married and they are going to have %d babies.\n", yourName, yourCrushesName, numberOfBabies);

    return 0;
}
