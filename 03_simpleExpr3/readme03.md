
## simpleExpr3  

SimpleExpr3.g4
```
grammar SimpleExpr3;

stat : expr ;

expr : <assoc=right> expr EXPO expr # Expo
     | expr MULT expr               # Mult
     | expr ADD  expr               # Add
     | INT                          # Int
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
> cd C:\...\simpleExpr3
> antlr4py3 SimpleExpr3.g4 -no-listener -visitor
```
test_SimpleExpr3.py
```
from antlr4 import *

from SimpleExpr3Lexer import SimpleExpr3Lexer
from SimpleExpr3Parser import SimpleExpr3Parser
from SimpleExpr3Visitor import SimpleExpr3Visitor

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
    
    
class Calc(SimpleExpr3Visitor):
    def __init__(self):
        super().__init__()
        
    def visitInt(self, ctx):
        print('Int:',int(ctx.INT().getText()))
        return int(ctx.INT().getText())        
        
    def visitAdd(self, ctx):        
        right = self.visit(ctx.expr(0))
        left = self.visit(ctx.expr(1))
        print('Add:','{} + {} = {}'.format(right, left, right + left))
        return right + left
        
    def visitMult(self, ctx):
        right = self.visit(ctx.expr(0))
        left = self.visit(ctx.expr(1))
        print('Mult:','{} * {} = {}'.format( right, left, right * left))
        return right * left
        
    def visitExpo(self, ctx):
        right = self.visit(ctx.expr(0))
        left = self.visit(ctx.expr(1))
        print('Expo:','{} ^ {} = {}'.format(right, left, right ** left))
        return right ** left        
        
    
file_name = 'test1.expr'
input_stream = FileStream(file_name)
lexer = SimpleExpr3Lexer(input_stream)
print('input_stream:')
print(input_stream)
print()
token_stream = CommonTokenStream(lexer)
parser = SimpleExpr3Parser(token_stream)
tree = parser.stat()

print('tree:')
lisp_tree_str = tree.toStringTree(recog=parser)
print(beautify_lisp_string(lisp_tree_str))
print()

print('calc:')
calc = Calc()
result = calc.visit(tree)
print()
print("result=", result)
```
test1.expr
```  
10+123*3
```

```
> python.exe test_SimpleExpr3.py
input_stream:
10+123*3

tree:
(stat 
   (expr 
      (expr 10) + 
      (expr 
         (expr 123) * 
         (expr 3))))

calc:
Int: 10
Int: 123
Int: 3
Mult: 123 * 3 = 369
Add: 10 + 369 = 379

result= 379
```

###  visitor

SimpleExpr3.g4    
各alternative に Label を付けます。  

```
expr : <assoc=right> expr EXPO expr # Expo
     | expr MULT expr               # Mult
     | expr ADD  expr               # Add
     | INT                          # Int
    
```

`antlr4py3 SimpleExpr3.g4 -no-listener -visitor`  

のコマンドを実行すると、 

SimpleExpr3Visitor.py (下記)  が生成されます。

```
# This class defines a complete generic visitor for a parse tree produced by SimpleExpr3Parser.

class SimpleExpr3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleExpr3Parser#stat.
    def visitStat(self, ctx:SimpleExpr3Parser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpr3Parser#Add.
    def visitAdd(self, ctx:SimpleExpr3Parser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpr3Parser#Expo.
    def visitExpo(self, ctx:SimpleExpr3Parser.ExpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpr3Parser#Mult.
    def visitMult(self, ctx:SimpleExpr3Parser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpr3Parser#Int.
    def visitInt(self, ctx:SimpleExpr3Parser.IntContext):
        return self.visitChildren(ctx)
```
class SimpleExpr3Visitor を継承して、次のようなクラスを作ります。  
```
class Calc(SimpleExpr3Visitor):
    def __init__(self):
        super().__init__()
        
    def visitInt(self, ctx):
        print('Int:',int(ctx.INT().getText()))
        return int(ctx.INT().getText())        
        
    def visitAdd(self, ctx):        
        right = self.visit(ctx.expr(0))
        left = self.visit(ctx.expr(1))
        print('Add:','{} + {} = {}'.format(right, left, right + left))
        return right + left
        
    def visitMult(self, ctx):
        right = self.visit(ctx.expr(0))
        left = self.visit(ctx.expr(1))
        print('Mult:','{} * {} = {}'.format( right, left, right * left))
        return right * left
        
    def visitExpo(self, ctx):
        right = self.visit(ctx.expr(0))
        left = self.visit(ctx.expr(1))
        print('Expo:','{} ^ {} = {}'.format(right, left, right ** left))
        return right ** left
```

class ParseTreeVisitor(object)  の method  visit(self, tree) は visitor.visitChildren(self) を返します。    

これにより、 下記の result が計算結果になります。   

```
calc = Calc()
result = calc.visit(tree)
```

file_name = 'test3.expr'   

```
input_stream:
2^3^4

tree:
(stat 
   (expr 
      (expr 2) ^ 
      (expr 
         (expr 3) ^ 
         (expr 4))))

calc:
Int: 2
Int: 3
Int: 4
Expo: 3 ^ 4 = 81
Expo: 2 ^ 81 = 2417851639229258349412352

result= 2417851639229258349412352
```

