#include <stdio.h>
#include <stdlib.h>

int main()
{

    int age;
    age = 16;
    printf("Mario ima %d godina.\n", age);
    /*Ovo je komentar*/
    //Ovo je isto komentar ali samo u jednom redu
    printf("Mario loves McDonald's!\n");
    printf("There will be a tab!\t");
    printf("You will hear a sound!\n\a");
    //Ovde %s je za neku rec, mi tu rec moramo da damo posle cele recenice da bi program radio.
    printf("%s is the best person ever!\n", "Mario");
    //Ako prvi put napisemo sta ce biti %s, a zaboravimo drugi put u recenici ispod, onda ce kompjuter sam uzeti onu varijablu iz prosle recenice
    printf("%s is the best person ever!\n");
    printf("%s is the best %s ever!\n", "Mario", "programmer");
    //Ovo isto mozes da uradis sa brojevima sa znakom %d
    printf("I ate %d cheeseburgers at McDonald's last night!\n", 4);
    printf("Pi is %.2f\n", 3.14159);
    printf("Pi is %.3f\n", 3.14159);
    printf("Pi is %.4f\n", 3.14159);
    printf("Pi is %.5f\n", 3.14159);
    char name[16] = "Mario Jovanovic";
    printf("My name is %s!\n", name);
    name[3] = 'k';
    printf("My name is %s!\n", name);
    char food[] = "Tuna";
    printf("The best food is %s!\n", food);
    strcpy(food, "bacon");
    printf("The best food is %s!\n", food);

    return 0;
}
