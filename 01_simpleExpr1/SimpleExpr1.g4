//antlr4py3 SimpleExpr1.g4

grammar SimpleExpr1;

// parser rules
stat : expr ;
expr : <assoc=right> expr EXPO expr
     | expr MULT expr
     | expr ADD  expr 
     | INT           
     ;

// lexer rules
EXPO : '^' ;
MULT : '*' ;
ADD  : '+' ;
INT : [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;
