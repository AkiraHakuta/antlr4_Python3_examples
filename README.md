## Python3 examples for ANTLR4  
## What is ANTLR4
[ANTLR4](http://www.antlr.org) is a parser generator.  

## Install (Windows)
- [Python3](https://www.python.org/downloads/)

- antlr4 python3 runtime (4.7.2)  
`> pip install antlr4-python3-runtime`
 - antlr-4.7.2-complete.jar ([Complete ANTLR 4.7.2 Java binaries jar](http://www.antlr.org/download.html))  
Make C:\Javalib and 
save antlr-4.7.2-complete.jar in C:\Javalib.  
- Java

## first example (simpleExpr1)   

SimpleExpr1.g4
```antlr
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
```

### How to create lexer and parser.  

#### using command prompt  
 Open Command Prompt and run bin/antlr4env.bat.  
The following command creates Python lexer and parser.
```
> cd C:\...\simpleExpr1
> antlr4py3 SimpleExpr1.g4
```  
#### using [Sublime Text 3](https://www.sublimetext.com/3)  
Tools -> Command Palette... -> Package Control: Install Package -> ANTLR syntax highlight  
Save Antlr4py3.sublime-build in User  
Antlr4py3.sublime-build  
```json
{
  "cmd":["java.exe", "-jar", "C:\\Javalib\\antlr-4.7.2-complete.jar", "-Dlanguage=Python3", "$file"],
  "selector": "source.antlr",
  "file_regex": "^error\\([0-9]*\\):\\s(.*?):([0-9]*):?([0-9]*):?\\s(.*)",
  "variants":[
      {
        "name": "no-listener -visitor",
        "cmd": ["java.exe", "-jar", "C:\\Javalib\\antlr-4.7.2-complete.jar", "-Dlanguage=Python3", "-no-listener", "-visitor", "$file"]
      },
      {
        "name": "o gen",
        "cmd": ["java.exe", "-jar", "C:\\Javalib\\antlr-4.7.2-complete.jar", "-Dlanguage=Python3", "-o", "gen", "$file"]
      },
      {
        "name": "visitor -no-listener -o gen",
        "cmd": ["java.exe", "-jar", "C:\\Javalib\\antlr-4.7.2-complete.jar", "-Dlanguage=Python3", "-visitor", "-no-listener", "-o", "gen", "$file"],
      }
  	]
}
```  
Open SimpleExpr1.g4  
Tools ->Build System -> Automatic  
Tools -> Build With... -> Antlr4py3  

test_SimpleExpr1.py  

```python
from antlr4 import *
from SimpleExpr1Lexer import SimpleExpr1Lexer
from SimpleExpr1Parser import SimpleExpr1Parser

# from https://github.com/antlr/antlr4/blob/master/runtime/Python3/bin/pygrun
# this is a python version of TestRig
def beautify_lisp_string(in_string):
    indent_size = 3
    add_indent = ' '*indent_size
    out_string = in_string[0]  # no indent for 1st (
    indent = ''
    for i in range(1, len(in_string)):
        if in_string[i] == '(' and in_string[i+1] != ' ':
            indent += add_indent
            out_string += "\n" + indent + '('
        elif in_string[i] == ')':
            out_string += ')'
            if len(indent) > 0:
                indent = indent.replace(add_indent, '', 1)
        else:
            out_string += in_string[i]
    return out_string
    
file_name = 'test1.expr'
input_stream = FileStream(file_name)
lexer = SimpleExpr1Lexer(input_stream)
print('input_stream:')
print(input_stream)
print()
token_stream = CommonTokenStream(lexer)
token_stream.fill()
print('tokens:')
for tk in token_stream.tokens:
    print(tk)
print()

parser = SimpleExpr1Parser(token_stream)
tree = parser.stat()
print('tree:')
lisp_tree_str = tree.toStringTree(recog=parser)
print(beautify_lisp_string(lisp_tree_str))
```

test1.expr
```  
10+123*3
```
Open Command Prompt  
```
> python.exe test_SimpleExpr1.py
input_stream:
10+123*3

tokens:
[@0,0:1='10',<4>,1:0]
[@1,2:2='+',<3>,1:2]
[@2,3:5='123',<4>,1:3]
[@3,6:6='*',<2>,1:6]
[@4,7:7='3',<4>,1:7]
[@5,8:7='<EOF>',<-1>,1:8]

tree:
(stat 
   (expr 
      (expr 10) + 
      (expr 
         (expr 123) * 
         (expr 3))))
```  

## Notes
(1) The Definitive ANTLR 4 Reference (by Terence Parr) eBook, Paper   
(2) [py3antlr4book](https://github.com/jszheng/py3antlr4book)  
