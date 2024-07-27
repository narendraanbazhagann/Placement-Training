#include <stdio.h>

void findDivisors(int num) {
    printf("Divisors of %d are: ", num);
    for (int i = 1; i <= num / 2; i++) {
        if (num % i == 0) {
            printf("%d ", i);
        }
    }
    printf("%d\n", num); // num itself is always a divisor
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    findDivisors(num);
    return 0;
}
