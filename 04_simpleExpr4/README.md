
## simpleExpr4  

SimpleExpr4.g4
```
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
```
Open Command Prompt and run bin/antlr4env.bat.  
The following command creates Python lexer and parser.

```
> cd C:\...\simpleExpr4
> antlr4py3 SimpleExpr4.g4
```
test_SimpleExpr4.py
```
from antlr4 import *

from SimpleExpr4Lexer import SimpleExpr4Lexer
from SimpleExpr4Parser import SimpleExpr4Parser
from SimpleExpr4Listener import SimpleExpr4Listener

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
    
    
class Calc(SimpleExpr4Listener):
    def __init__(self):
        super().__init__()
        
    def exitInt(self, ctx):
        ctx.value=int(ctx.INT().getText())
        print('Int: ',int(ctx.INT().getText()))

    def exitAdd(self, ctx):
        ctx.value = ctx.expr(0).value + ctx.expr(1).value        
        print('Add:','{} + {} = {}'.format(ctx.expr(0).value, ctx.expr(1).value, ctx.value))
        
    def exitMult(self, ctx):
        ctx.value = ctx.expr(0).value * ctx.expr(1).value
        print('Mult:','{} * {} = {}'.format(ctx.expr(0).value, ctx.expr(1).value, ctx.value))
        
    def exitExpo(self, ctx):
        ctx.value = ctx.expr(0).value ** ctx.expr(1).value
        print('Expo:','{} ^ {} = {}'.format(ctx.expr(0).value, ctx.expr(1).value, ctx.value))

    def exitStat(self, ctx):
        ctx.result=int(ctx.expr().value)
        
        
    
file_name = 'test1.expr'
input_stream = FileStream(file_name)
lexer = SimpleExpr4Lexer(input_stream)
print('input_stream:')
print(input_stream)
print()    
token_stream = CommonTokenStream(lexer)
parser = SimpleExpr4Parser(token_stream)
tree = parser.stat()

print('tree:')
lisp_tree_str = tree.toStringTree(recog=parser)
print(beautify_lisp_string(lisp_tree_str))
print()

calc = Calc()
walker = ParseTreeWalker()
walker.walk(calc, tree)
print()
print('result = ', tree.result)
```
test1.expr
```  
10+123*3
```

```
> python.exe test_SimpleExpr4.py
input_stream:
10+123*3

tree:
(stat 
   (expr 
      (expr 10) + 
      (expr 
         (expr 123) * 
         (expr 3))))

Int:  10
Int:  123
Int:  3
Mult: 123 * 3 = 369
Add: 10 + 369 = 379

result =  379
```

下記 (SimpleExpr4.g4)  のように、各parser rule に locals[result],  locals[value] を挿入すると、    

```
stat locals[result] // or returns[result]
    : expr ;

expr locals[value] // or returns[value]
    : <assoc=right> expr EXPO expr # Expo
     | expr MULT expr              # Mult
     | expr ADD  expr              # Add
     | INT                         # Int
     ;    
```

class SimpleExpr4Parser ( Parser ) に インスタンス変数 が挿入されます。  

```
class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            
.....

class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
```

これを使って、計算経過・結果を次のようなプログラムで保存します。  

```
class Calc(SimpleExpr4Listener):
    def __init__(self):
        super().__init__()
        
    def exitInt(self, ctx):
        ctx.value=int(ctx.INT().getText())
        print('Int: ',int(ctx.INT().getText()))

    def exitAdd(self, ctx):
        ctx.value = ctx.expr(0).value + ctx.expr(1).value        
        print('Add:','{} + {} = {}'.format(ctx.expr(0).value, ctx.expr(1).value, ctx.value))
        
    def exitMult(self, ctx):
        ctx.value = ctx.expr(0).value * ctx.expr(1).value
        print('Mult:','{} * {} = {}'.format(ctx.expr(0).value, ctx.expr(1).value, ctx.value))
        
    def exitExpo(self, ctx):
        ctx.value = ctx.expr(0).value ** ctx.expr(1).value
        print('Expo:','{} ^ {} = {}'.format(ctx.expr(0).value, ctx.expr(1).value, ctx.value))

    def exitStat(self, ctx):
        ctx.result=int(ctx.expr().value)
```
これにより、 下記の result が計算結果になります。   

```
calc = Calc()
walker = ParseTreeWalker()
walker.walk(calc, tree)
print()
print('result = ', tree.result)
```
