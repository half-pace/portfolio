%{
#include <stdio.h>
int chars = 0;
int words = 0;
int lines = 0;    
%}

%%
\n     { lines++; chars++; }
[a-zA-Z0-9]+ { words++; chars += yyleng; }
.   { chars++; }
%%

int main(int argc, char *argv[]) {
    if(argc > 1){
        yyin = fopen(argv[1], "r");
    }

    yylex();
    printf("Characters: %d\n", chars);
    printf("Words: %d\n", words);
    printf("Lines: %d\n", lines);
    return 0;
}