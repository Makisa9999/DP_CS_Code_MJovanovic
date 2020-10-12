#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("***************************************WELCOME***************************************\n");
    printf("I made this program to help you calculate the interest.\n");
    float amountMoney;
    float numberYears;
    float interestRate;
    float finalAmount;
    printf("What is the amount of money that you would like to deposit?\n");
    scanf("%f", &amountMoney);
    printf("How many years do you want this money to stay in the bank?");
    scanf("%f", &numberYears);
    printf("What is the interest rate that you are going to have?");
    scanf("%f", &interestRate);
    printf("The final amount that you are going to have after %.0f years is: 1", numberYears);
    printf("%.2f", amountMoney * pow(interestRate, numberYears));



    return 0;
}
