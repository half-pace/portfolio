//yacc first
//bison -d filename.y -> y.tab.h and y.tab.c
//then lex in include use eihter y.tab.h or filename.tab.h
//then flex filename.l -> lex.yy.c
//gcc lex.yy.c a.tab.c -lfl
//then lex

%{
#include <stdio.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);
%}

%token NUMBER

%left '+' '-
%left '*' '/'
%left '(' ')'

%%
input:
    | input line
    ;

line:
    '\n'
    | exp '\n' { printf("Result: %d\n", $1); }
    ;

exp:
    expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr {
        if ($3 == 0) {
            printf("Division by zero\n");
            exit(1);
        }
        $$ = $1 / $3;
    }
    | '(' exp ')' { $$ = $2; }
    | NUMBER { $$ = $1; }
    ;

%%

void yyerror(const char *s){
    fprintf(stderr, "Error: %s\n", s);
}

int main(void){
    printf("Enter an expression:\n");
    yyparse();
    return 0;
}



%{
#include <stdio.h>
%}

%%
[0-9]+ {yylval = atoi(yytext); return NUMBER;}
[ \t]  ; // ignore whitespace
\n     return '\n'; // return newline as token
.      return yytext[0]; // return any other character as token
%%

int yywrap() {
return 1; // indicate end of input
}