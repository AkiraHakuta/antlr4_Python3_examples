// antlr4py3 PyEmbInTxt.g4 -o gen

grammar PyEmbInTxt;

stat : ( py | SP | OTHER )*;

py : PYCODE # pyc
    | PYPRN # pyp
    ;

PYCODE : '\\begin{pyc}' .*? '\\end{pyc}' ;
PYPRN  : '\\pyp{' .*? '/pyp}'  ;

SP : [ ] ;
COMMENT : '///*' .*? '*///'   -> skip ;
LINE_COMMENT : '///' ~[\r\n]* -> skip ;
OTHER :  . ;