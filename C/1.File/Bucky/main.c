#include <stdio.h>
#include <stdlib.h>
#define MYNAME "Mario Jovanovic"


int main()
{
    char userName[30];
    char troll[5] = "Dick";
    printf("************************WELCOME****************************\n");
    printf("Enter Your Name: ");
    scanf("%s", userName);
    printf("Your name is %s.\n", troll);
    system("pause");
    printf("JK its %s.\n", userName);
    system("pause");
    printf("Owner of this program is %s.\n", MYNAME);
    return 0;
}
