
## Expr  

Expr.g4
```antlr
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
```
Open Command Prompt and run bin/antlr4env.bat.  
The following command creates Python lexer and parser.

```
> cd C:\...\Expr
> antlr4py3 Expr.g4 -no-listener -visitor
```
test_Expr.py
```python
from antlr4 import *

from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


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
    
    
class Calc(ExprVisitor):
    def __init__(self):
        super().__init__()    
        self.result = ''
        self.id_memory = {}
        
    def visitReturnValue(self, ctx):
        self.result += str(self.visit(ctx.expr())) + '\n'
        return self.result
        
    def visitInteger(self, ctx):
        return int(ctx.INT().getText()) 
        
    def visitFloat(self, ctx):
        return float(ctx.FLOAT().getText()) 
        
    def visitAdd_sub(self, ctx):        
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            result = left + right
        else:
            result = left - right
        return result
        
    def visitMul_div(self, ctx):        
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            result = left * right
        else:
            result = left / right
        return result
        
    def visitExpo(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        result = left ** right
        return result
        
    def visitParen(self, ctx):
        return self.visit(ctx.expr())
        
    def visitAssignment(self, ctx):
        self.id_memory[ctx.ID().getText()] = self.visit(ctx.expr())
        print('id_memory=',self.id_memory)
        
    def visitVar(self, ctx):
        return self.id_memory[ctx.ID().getText()]
        
    def visitPm_integer(self, ctx):
        result = self.visit(ctx.expr())
        if ctx.op.text == '-':
            result = (-1) * result
        return result        

    
file_name = 'test.expr'
input_stream = FileStream(file_name)
print('input_stream:')
print(input_stream)
print()
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()
print('tokens:')
for tk in token_stream.tokens:
    print(tk)
print()
parser = ExprParser(token_stream)
tree = parser.prog()

print('tree:')
lisp_tree_str = tree.toStringTree(recog=parser)
print(beautify_lisp_string(lisp_tree_str))
print()

print('calc:')
calc = Calc()
result = calc.visit(tree)
print()
print('result:')
print(result)

```
test.expr
```  
-13.57+14.8/2.0
a10=3
xx=+50-8*((5+4)-3)

a10^2*xx

```
Open Command Prompt  
```
> python.exe test_SimpleExpr5.py
input_stream:
-13.57+14.8/2.0
a10=3
xx=+50-8*((5+4)-3)

a10^2*xx


tokens:
[@0,0:0='-',<6>,1:0]
[@1,1:5='13.57',<10>,1:1]
[@2,6:6='+',<5>,1:6]
[@3,7:10='14.8',<10>,1:7]
[@4,11:11='/',<4>,1:11]
[@5,12:14='2.0',<10>,1:12]
[@6,15:15='\n',<12>,1:15]
......
......
[@32,47:47='*',<3>,5:5]
[@33,48:49='xx',<9>,5:6]
[@34,50:50='\n',<12>,5:8]
[@35,51:50='<EOF>',<-1>,6:0]

tree:
(prog 
   (stat 
      (expr 
         (expr - 
            (expr 13.57)) + 
         (expr 
            (expr 14.8) / 
            (expr 2.0))) \n) 
   (stat a10 = 
      (expr 3) \n) 
   (stat xx = 
      (expr 
         (expr + 
            (expr 50)) - 
         (expr 
            (expr 8) * 
            (expr ( 
               (expr 
                  (expr ( 
                     (expr 
                        (expr 5) + 
                        (expr 4)) )) - 
               (expr 3)) )))) \n) 
   (stat \n) 
   (stat 
      (expr 
         (expr 
            (expr a10) ^ 
            (expr 2)) * 
         (expr xx)) \n))

calc:
id_memory= {'a10': 3}
id_memory= {'a10': 3, 'xx': 2}

result:
-6.17
18
```
