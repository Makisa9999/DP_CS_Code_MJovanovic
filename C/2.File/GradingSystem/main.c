#include <stdio.h>
#include <stdlib.h>

int main()
{
    int grade1;
    int grade2;
    int grade3;

    printf("Grade 1: ");
    scanf(" %d", &grade1);
    printf("Grade 2: ");
    scanf(" %d", &grade2);
    printf("Grade 3: ");
    scanf(" %d", &grade3);

    // else if ti daje da kompjuter testira i da vidi gde se uklapa;
    float avg = ((float)grade1 + (float)grade2 + (float)grade3) / 3;
    printf("Average: %.1f\n", avg);

    if (avg >= 85) {
        printf("Grade: A!");
    }else if (avg >= 70) {
        printf("Grade: B!");
    }else if (avg >= 50) {
        printf("Grade: C!");
    }else if (avg >= 30) {
        printf("Grade: D!");
    }else {
        printf("You are dumb!");
    }


    return 0;
}
