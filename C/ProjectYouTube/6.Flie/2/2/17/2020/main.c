#include <stdio.h>
#include <stdlib.h>

int main()
{
     int currentYear;
        int birthYear;
        int Years1;
        int Years2;
        char birthday[5];
        Years1 = currentYear - birthYear;
        Years2 = currentYear - birthYear - 1;
    printf("Koja je godina danas?");
    scanf(" %d", &currentYear);
    printf("Koje godine si se ti rodio?");
    scanf(" %d", &birthYear);
    printf("Da li si slavio ove godine rodjendan? (D/N)");
    scanf(" %c", &birthday);
    if (birthday == 'D'){
        printf(" Imas godina");
    }
    if (birthday == 'N') {
        printf("Imas godina.");
    }
    printf("done\n");
    return 0;
}
