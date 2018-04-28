
## simpleExpr2  

SimpleExpr2.g4
```
grammar SimpleExpr2;

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
> cd C:\...\simpleExpr2
> antlr4py3 SimpleExpr2.g4
```
test_SimpleExpr2.py
```
from antlr4 import *

from SimpleExpr2Lexer import SimpleExpr2Lexer
from SimpleExpr2Parser import SimpleExpr2Parser
from SimpleExpr2Listener import SimpleExpr2Listener

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
    
class Calc(SimpleExpr2Listener):
    def __init__(self):
        super().__init__()
        self.memory = {}
        self.result = None
        
    def exitInt(self, ctx):
        self.memory[ctx]=int(ctx.INT().getText())
        print('Int:memory=',self.memory)
        
    def exitAdd(self, ctx):
        right = self.memory[ctx.expr(0)]
        left  = self.memory[ctx.expr(1)]
        self.memory[ctx]=right + left
        print('Add:memory=',self.memory)
        
    def exitMult(self, ctx):
        right = self.memory[ctx.expr(0)]
        left  = self.memory[ctx.expr(1)]
        self.memory[ctx]=right * left
        print('Mult:memory=',self.memory)
        
    def exitExpo(self, ctx):
        right = self.memory[ctx.expr(0)]
        left  = self.memory[ctx.expr(1)]
        self.memory[ctx]=right ** left
        print('Expo:memory=',self.memory)    
        
    def exitStat(self, ctx):
        self.result=self.memory[ctx.expr()]
        
    
file_name = 'test1.expr'
input_stream = FileStream(file_name)
lexer = SimpleExpr2Lexer(input_stream)
print('input_stream:')
print(input_stream)
print()
token_stream = CommonTokenStream(lexer)
parser = SimpleExpr2Parser(token_stream)
tree = parser.stat()

print('tree:')
lisp_tree_str = tree.toStringTree(recog=parser)
print(beautify_lisp_string(lisp_tree_str))
print()

print('calc:')
calc = Calc()
walker = ParseTreeWalker()
walker.walk(calc, tree)
print()
print('result =', calc.result)
```
test1.expr
```  
10+123*3
```

```
> python.exe test_SimpleExpr2.py
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
Int:memory= {<SimpleExpr2Parser.SimpleExpr2Parser.IntContext object at 0x0000013E54E45320>: 10}
......
......

result = 379
```

###  listener

SimpleExpr2.g4   
各alternative に Label を付けることができます。  
付ける場合は、その parser rule のすべての alternative に付けなければなりません。  

```
expr : <assoc=right> expr EXPO expr # Expo
     | expr MULT expr               # Mult
     | expr ADD  expr               # Add
     | INT                          # Int
     ;
```

SimpleExpr2Listener.py (下記)  が生成されます。  

```
# This class defines a complete listener for a parse tree produced by SimpleExpr2Parser.
class SimpleExpr2Listener(ParseTreeListener):

    # Enter a parse tree produced by SimpleExpr2Parser#stat.
    def enterStat(self, ctx:SimpleExpr2Parser.StatContext):
        pass

    # Exit a parse tree produced by SimpleExpr2Parser#stat.
    def exitStat(self, ctx:SimpleExpr2Parser.StatContext):
        pass
        
     .......
     .......
     .......

    # Enter a parse tree produced by SimpleExpr2Parser#Int.
    def enterInt(self, ctx:SimpleExpr2Parser.IntContext):
        pass

    # Exit a parse tree produced by SimpleExpr2Parser#Int.
    def exitInt(self, ctx:SimpleExpr2Parser.IntContext):
        pass
```

```
calc = Calc()
walker = ParseTreeWalker()
walker.walk(calc, tree)
```
で tree を一周回ることができます。  

同じ枝を 例えば enterAdd(), enterAdd() で2回 (入るときと出るとき) 通過します。 

ここで計算をさせると、電卓ができます。  

class SimpleExpr2Listener を継承して、次のようなクラスを作ります。  

```
class Calc(SimpleExpr2Listener):
    def __init__(self):
        super().__init__()
        self.memory = {}
        self.result = None
        
    def exitInt(self, ctx):
        self.memory[ctx]=int(ctx.INT().getText())
        print('Int:memory=',self.memory)
        
    def exitAdd(self, ctx):
        right = self.memory[ctx.expr(0)]
        left  = self.memory[ctx.expr(1)]
        self.memory[ctx]=right + left
        print('Add:memory=',self.memory)
        
    def exitMult(self, ctx):
        right = self.memory[ctx.expr(0)]
        left  = self.memory[ctx.expr(1)]
        self.memory[ctx]=right * left
        print('Mult:memory=',self.memory)
        
    def exitExpo(self, ctx):
        right = self.memory[ctx.expr(0)]
        left  = self.memory[ctx.expr(1)]
        self.memory[ctx]=right ** left
        print('Expo:memory=',self.memory)    
        
    def exitStat(self, ctx):
        self.result=self.memory[ctx.expr()]
```

計算経過・結果を保存する場所がないので、  

インスタンス変数   

```
self.memory = {}
self.result = None
```

を用意します。  

tree を1周回ると `calc.result`に最終的な計算結果が入ります。  

file_name = 'test1.expr'  　

```
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
Int:memory= {<SimpleExpr2Parser.SimpleExpr2Parser.IntContext object at 0x000002598F305358>: 10}
.......
.......

result = 379
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
Int:memory= {<SimpleExpr2Parser.SimpleExpr2Parser.IntContext object at 0x00000181405550B8>: 2}
.......
.......

result = 2417851639229258349412352
```

