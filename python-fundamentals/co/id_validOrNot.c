#include <stdio.h>
#include <ctype.h>

//to detect whether a given identifier is valid or not
int isValidIdentifier(const char *str) {
    // Check if the first character is a letter or underscore
    if (!isalpha(str[0]) && str[0] != '_') {
        return 0; // Invalid identifier
    }

    // Check the rest of the characters
    for (int i = 1; str[i] != '\0'; i++) {
        if (!isalnum(str[i]) && str[i] != '_') {
            return 0; // Invalid identifier
        }
    }

    return 1; // Valid identifier
}