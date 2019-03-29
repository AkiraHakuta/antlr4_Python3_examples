
## simpleExpr5  

SimpleExpr5.g4
```antlr
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
```
Open Command Prompt and run bin/antlr4env.bat.  
The following command creates Python lexer and parser.

```
> cd C:\...\simpleExpr5
> antlr4py3 SimpleExpr5.g4 
```
test_SimpleExpr5.py
```python
from antlr4 import *

from SimpleExpr5Lexer import SimpleExpr5Lexer
from SimpleExpr5Parser import SimpleExpr5Parser

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
lexer = SimpleExpr5Lexer(input_stream)
print('input_stream:')
print(input_stream)
print()    
token_stream = CommonTokenStream(lexer)
parser = SimpleExpr5Parser(token_stream)
tree = parser.stat()

print('tree:')
lisp_tree_str = tree.toStringTree(recog=parser)
print(beautify_lisp_string(lisp_tree_str))
print()

print('result = ',tree.result)
```
test1.expr
```  
10+123*3
```
Open Command Prompt  
```
> python.exe test_SimpleExpr5.py
input_stream:
10+123*3

tree:
(stat 
   (expr 
      (expr 10) + 
      (expr 
         (expr 123) * 
         (expr 3))))

result =  379
```

上記 (SimpleExpr5.g4)  のように記述すると、  

class SimpleExpr5Parser ( Parser ) に code を挿入することができます。  

単に書き込むだけで、正しい Python のコードであるかのチェックはしません。  

プログラムを実行して不具合があった場合は、SimpleExpr5Parser.py を開いて確認する必要があります。  

 SimpleExpr5Parser.py

```python
# Generated from SimpleExpr5.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


#import ???

......
class SimpleExpr5Parser ( Parser ):

    ......
    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        .....
        
    def eval(self, left, op, right):
        if   SimpleExpr5Parser.EXPO == op.type:
            return left ** right
        elif SimpleExpr5Parser.MULT == op.type:
            return left * right
        elif SimpleExpr5Parser.ADD == op.type:
            return left + right
        else:
            return 0
            
     .....
    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self._expr = None # ExprContext
     ......
     
     class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            ......
            
     def expr(self, _p:int=0):
        ......
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            localctx._INT = self.match(SimpleExpr5Parser.INT)
            localctx.value = (0 if localctx._INT is None else int(localctx._INT.text))
            ......
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    .....
                    if la_ == 1:
                        localctx = SimpleExpr5Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        .....
                        localctx.b = self.expr(4)
                        localctx.value = self.eval(localctx.a.value, localctx._EXPO, localctx.b.value)
                        pass

                    elif la_ == 2:
                        localctx = SimpleExpr5Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        ......
                        localctx.b = self.expr(4)
                        localctx.value = self.eval(localctx.a.value, localctx._MULT, localctx.b.value)
                        pass

                    elif la_ == 3:
                        localctx = SimpleExpr5Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        
                        localctx.b = self.expr(3)
                        localctx.value = self.eval(localctx.a.value, localctx._ADD,  localctx.b.value)
                        pass
```

 class SimpleExpr5Parser に挿入したcode で計算をしてくれます。  

このお陰で test_SimpleExpr5.py はとてもシンプルになります。  
でも、それが良いのか否かは別問題です。  
複雑な grammar はとても読みにくいものです。  

```python
.....
token_stream = CommonTokenStream(lexer)
parser = SimpleExpr5Parser(token_stream)
tree = parser.stat()
.....
print('result = ',tree.result)
```

tree.result が計算結果になります。    
