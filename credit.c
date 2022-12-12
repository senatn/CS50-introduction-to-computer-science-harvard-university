#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long creditCartNumber;

    do
    {
        creditCartNumber = get_long("Number: ");
    }
    while (creditCartNumber < 0);

    long testNumber = creditCartNumber;
    int lastDigit = 0;
    int sum = 0;

    while (testNumber > 0)
    {
        lastDigit = testNumber % 10;
        sum = sum + lastDigit;
        testNumber = testNumber / 100;
    }

    long testNumber2 = creditCartNumber / 10;
    int lastDigit2 = 0;

    while (testNumber2 > 0)
    {
        lastDigit2 = testNumber2 % 10;
        sum = sum + (lastDigit2 * 2 % 10) + (lastDigit2 * 2 / 10);
        testNumber2 = testNumber2 / 100;
    }

    // printf("%d\n", sum );

    long testNumber3 = creditCartNumber;
    int ccnLenght = 0;

    while (testNumber3 > 0)
    {
        testNumber3 = testNumber3 / 10;
        ccnLenght++;
    }

    // printf("%d\n", ccnLenght );

    int firsDigit = creditCartNumber / pow(10, (ccnLenght - 1));

    // printf("%d\n", firsDigit );

    int firsTwoDigit = creditCartNumber / pow(10, (ccnLenght - 2));

    // printf("%d\n", firsTwoDigit );

    if (sum % 10 == 0 && (firsTwoDigit == 34 || firsTwoDigit == 37) && ccnLenght == 15)
    {
        printf("AMEX\n");
    }

    else if (sum % 10 == 0 && (50 < firsTwoDigit && firsTwoDigit < 56) && ccnLenght == 16)
    {
        printf("MASTERCARD\n");
    }

    else if (sum % 10 == 0 &&  firsDigit == 4 && (ccnLenght == 16 || ccnLenght == 13))
    {
        printf("VISA\n");
    }

    else
    {
        printf("INVALID\n");
    }

}