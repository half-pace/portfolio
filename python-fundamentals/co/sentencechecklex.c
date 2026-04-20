//sentence checking

%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
voir yyerror(const char *s);
%}

%token NOUN VERB ARTICLE

%%
sentence: subject predicate object {print("Valid sentence\n");};
subject: NOUN;
predicate: VERB;
object: NOUN | ARTICLE NOUN;

%%

void yyerror(const char *s){
    printf("Invalid sentence\n");
}

int main(){
    printf("Enter a sentence:\n");
    yyparse();
    return 0;
}



%{
#include "filename.tab.h"
%}

%%
"RAM"|"HE" { return NOUN; }
"eats"|"likes" { return VERB; }
"a"|"an"|"the" { return ARTICLE; }
"mango"|"apple" { return NOUN; }
[ \t\n]+ { /* ignore whitespace */ }
. {return yytext[0];}
%%

int yywrap(){
    return 1;
}