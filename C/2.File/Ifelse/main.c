#include <stdio.h>
#include <stdlib.h>

int main()
{
    char lastName[20];

    printf("Enter you last name: \n");
    scanf(" %s", lastName);

    // Uvek moras da pises uppercase letters prvo slovo u prezimenu
    // (test) ? (True) : (False) ;
    (lastName[0] < 'M') ? printf("Blue Team\n") : printf("Red Team\n") ;

    int friends;
    printf("How many friends do you have?\n");
    scanf(" %d", &friends);
    printf("You have %d friend%s!\n", friends, (friends != 1) ? "s" : "");
    return 0;
}
