// antlr4py3 SimpleExpr4.g4 

grammar SimpleExpr4;

stat locals[result] // or returns[result]
    : expr ;

expr locals[value] // or returns[value]
    : <assoc=right> expr EXPO expr # Expo
     | expr MULT expr              # Mult
     | expr ADD  expr              # Add
     | INT                         # Int
     ;

EXPO : '^' ;
MULT : '*' ;
ADD  : '+' ;
INT : [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;
