//vowel and consonant lexemes

%{
#include <stdio.h>
int consonants = 0;
int vowels = 0;
%}

%%
[aAeEiIoOuU] { vowels++; }
[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z] { consonants++; }
.   { /* ignore other characters */ }
%%

int main() {
    yylex();
    printf("Vowels: %d\n", vowels);
    printf("Consonants: %d\n", consonants);
    return 0;
}