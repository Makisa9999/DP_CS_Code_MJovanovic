#include <stdio.h>
#include <stdlib.h>

int main()
{
    float avgProfit;
    int priceOfPumpkin = 10;
    int sales = 59;
    int daysWorked = 7;
    // da bi mogao komp da izracuna profit u decimalama sa integerima moras da promenis variablu u float tako sto ces dodati "(float)" ispred imena variable koju menjas
    avgProfit = ( (float)priceOfPumpkin * (float)sales) / (float)daysWorked;
    printf("Average daily profit: $%.2f", avgProfit);
    return 0;
}
