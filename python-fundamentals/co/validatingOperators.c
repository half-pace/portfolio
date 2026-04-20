#include <stdio.h>
#include <string.h>

//for validating operators
int isValidOperator(const char *str) {
    // List of valid operators
    const char *validOperators[] = {
        "+", "-", "*", "/", "%", "++", "--", "==", "!=", "<", ">", "<=", ">=", "&&", "||", "!", "&", "|", "^", "~", "<<", ">>"
    };
    int numOperators = sizeof(validOperators) / sizeof(validOperators[0]);

    // Check if the input string matches any of the valid operators
    for (int i = 0; i < numOperators; i++) {
        if (strcmp(str, validOperators[i]) == 0) {
            return 1; // Valid operator
        }
    }

    return 0; // Invalid operator
}