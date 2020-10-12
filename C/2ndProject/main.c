#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 4 + 2 * 6;
    printf("Result: %d\n", a);

    int b = (4 + 2) * 6;
    printf("Result with brackets: %d\n", b);

    int aa;
    int ab;
    int ac;

    aa = ab = ac = 100;
    printf("aa = %d ab = %d ac = %d\n", aa, ab, ac);

    float age1, age2, age3, average;
    age1 = age2 = 4.0;

    printf("Enter your age\n");
    scanf("%f", &age3);

    average = (age1 + age2 + age3) / 3;
    printf("The average of these ages is %f\n", average);

    float old1, old2, old3, average1;
    old1 = old2 = 16;
    printf("Enter your age\n");
    scanf("%f", &old3);
    average1 = (old1 + old2+ old3) / 3;
    printf("The average age in the group is %f.\n", average1);

    return 0;
}
