#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    // Remove the newline character if present
    str[strcspn(str, "\n")] = '\0';

    if (str[0] == '/' && str[1] == '/') {
        printf("This is a comment.\n");
    } else {
        printf("This is not a comment.\n");
    }

    return 0;
}