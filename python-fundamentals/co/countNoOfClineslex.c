//count number of comment lines in a c program and eliminate them and copy that program to a separate file

%{
#include <stdio.h>
int comment_line_count = 0;    
%}

%%
"//".* { comment_line_count++; } // Count single-line comments
"/*"([^*]|[*]+[^*/])*[*]+"/" { comment_line_count++; } // Count multi-line comments
.|\n  { fprintf(yyout, "%s", yytext);}
%%

int main(int argc, char *argv[]){
    if (argc < 2) return 1;
    yyin = fopen(argv[1], "r");
    yyout = fopen("output.c", "w");
    yylex();
    printf("Number of comment lines: %d\n", comment_line_count);
    return 0;
}