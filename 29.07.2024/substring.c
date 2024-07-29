#include <stdio.h>
#include <string.h>

int isSubstring(char* s1, char* s2) {
    if (strstr(s1, s2) != NULL)
        return 1;
    return 0;
}

int main() {
    char s1[100], s2[100];

    printf("Enter the main string: ");
    gets(s1);

    printf("Enter the substring: ");
    gets(s2);

    if (isSubstring(s1, s2))
        printf("'%s' is a substring of '%s'.\n", s2, s1);
    else
        printf("'%s' is not a substring of '%s'.\n", s2, s1);

    return 0;
}
