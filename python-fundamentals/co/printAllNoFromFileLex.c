%{
#include <stdio.h>
%}

%%
[+-]?[0-9]*\.?[0-9]+    { printf("%s\n", yytext); }
.   { /* ignore other characters */ }
%%

int main(int argc, char *argv[]) {
    if(argc > 1){
        yyin = fopen(argv[1], "r");
    }
    yylex();
    return 0;
}