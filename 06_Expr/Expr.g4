// antlr4py3 Expr.g4 -no-listener -visitor

grammar Expr;

prog:   stat+ ; 

stat:   expr NEWLINE          # returnValue            
    |   ID '=' expr NEWLINE   # assignment    
    |   NEWLINE               # ignore
    ;

expr:  <assoc=right> expr '^' expr # expo
    |  expr op=('*'|'/') expr      # mul_div
    |  op=('+'|'-') expr           # pm_integer
    |   expr op=('+'|'-') expr     # add_sub
    |   FLOAT                      # float
    |   INT                        # integer
    |   ID                         # var
    |   '(' expr ')'               # paren
    ;

ID  : ALPHABET(ALPHABET|DIGIT)* ;
FLOAT:  DIGIT*  '.' DIGIT+ ;
INT : DIGIT+ ;
fragment ALPHABET: [a-zA-Z] ;
fragment DIGIT: [0-9] ;
NEWLINE:'\r'? '\n' ;
WS  :   [ \t]+ -> skip ;
