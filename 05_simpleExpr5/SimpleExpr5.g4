// antlr4py3 SimpleExpr5.g4 

grammar SimpleExpr5;

@parser::header{
#import ???
}

@parser::members{
def eval(self, left, op, right):
    if   SimpleExpr5Parser.EXPO == op.type:
        return left ** right
    elif SimpleExpr5Parser.MULT == op.type:
        return left * right
    elif SimpleExpr5Parser.ADD == op.type:
        return left + right
    else:
        return 0
}

stat returns[result]
    : expr {$result = $expr.value} 
    ;

expr returns[value] // not locals[value]
    : <assoc=right> a=expr EXPO b=expr {$value = self.eval($a.value, $EXPO, $b.value)}
     | a=expr MULT b=expr              {$value = self.eval($a.value, $MULT, $b.value)}
     | a=expr ADD  b=expr              {$value = self.eval($a.value, $ADD,  $b.value)}
     | INT                             {$value = $INT.int}
     ;

EXPO : '^' ;
MULT : '*' ;
ADD  : '+' ;
INT : [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;
