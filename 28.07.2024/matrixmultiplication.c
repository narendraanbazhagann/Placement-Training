#include <stdio.h>

int main() {
    int m, n, p, q, i, j, k;
    int first[10][10], second[10][10], result[10][10];

    printf("Enter rows and columns for first matrix: ");
    scanf("%d %d", &m, &n);
    printf("Enter rows and columns for second matrix: ");
    scanf("%d %d", &p, &q);

    if (n != p) {
        printf("Error! column of first matrix not equal to row of second.\n");
        return -1;
    }

    printf("Enter elements of first matrix:\n");
    for (i = 0; i < m; ++i) {
        for (j = 0; j < n; ++j) {
            scanf("%d", &first[i][j]);
        }
    }

    printf("Enter elements of second matrix:\n");
    for (i = 0; i < p; ++i) {
        for (j = 0; j < q; ++j) {
            scanf("%d", &second[i][j]);
        }
    }

    for (i = 0; i < m; ++i) {
        for (j = 0; j < q; ++j) {
            result[i][j] = 0;
            for (k = 0; k < n; ++k) {
                result[i][j] += first[i][k] * second[k][j];
            }
        }
    }

    printf("Resultant matrix:\n");
    for (i = 0; i < m; ++i) {
        for (j = 0; j < q; ++j) {
            printf("%d ", result[i][j]);
            if (j == q - 1) {
                printf("\n");
            }
        }
    }

    return 0;
}
