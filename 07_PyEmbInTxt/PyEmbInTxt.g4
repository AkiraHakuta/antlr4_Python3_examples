// antlr4py3 PyEmbInTxt.g4 -o gen

grammar PyEmbInTxt;

stat : ( py | SP | OTHER )*;

py : PYCODE # Pycd
    | PYPRN # Pypr
    ;

PYCODE : '\\pycode{' .*? '/code}' ;
PYPRN  : '\\pyprn{' .*? '/prn}'  ;

SP : [ ] ;
COMMENT : '///*' .*? '*///'   -> skip ;
LINE_COMMENT : '///' ~[\r\n]* -> skip ;
OTHER :  . ;