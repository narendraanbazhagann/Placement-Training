#include <stdio.h>

int main() {
    int n;
    printf("Enter the height of the zigzag pattern: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i % 2 == 0) {
                printf("* ");
            } else {
                if (j == 0 || j == n - 1) {
                    printf("* ");
                } else {
                    printf("  ");
                }
            }
        }
        printf("\n");
    }

    return 0;
}
