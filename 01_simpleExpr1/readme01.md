
## simpleExpr1  

SimpleExpr1.g4
```
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
Open Command Prompt and run bin/antlr4env.bat.  
The following command creates Python lexer and parser.

```
> cd C:\...\simpleExpr1
> antlr4py3 SimpleExpr1.g4
```
test_SimpleExpr1.py
```
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

print('tokens:')
for tk in token_stream.tokens:
    print(tk)
print()

print('tree:')
lisp_tree_str = tree.toStringTree(recog=parser)
print(beautify_lisp_string(lisp_tree_str))
```
test1.expr
```  
10+123*3
```

```
> python.exe test_SimpleExpr1.py
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



### antlr4とは  
antlr4はLL構文解析に基づく parser generator です。  
Java で動きます。  
Java, C++, Python(2 and 3), ...  のコードを生成することができます。  
このrepositoryは Python3 を用いた使用例です。  
参考にしたのは、  
(1) The Definitive ANTLR 4 Reference (by Terence Parr) 邦訳なし、eBook あり    
(2) [py3antlr4book](https://github.com/jszheng/py3antlr4book)    

(1) が Bible です。 私にとっては、難解な書籍でした。  
ほとんどの code を Python で確認はしましたが、不明の点がまだ多数あります。  

### grammar
SimpleExpr1.g4は EBNF に基づいて書かれています。  
正規表現を知っている方なら上記の文法を見て、なんとなく分かると思います。  
&nbsp;  
parser rule name は小文字、
lexer rule name は大文字のアルファベットではじめなければならない。  
lexer, parser 共に、定義された順に高い優先度が与えられます。  
&nbsp;  

### lexer.py, parser.py の生成  
コマンドプロンプトで  
```
bin/antlr4env.bat
cd ...\SimpleExpr1   
antlr4py3 SimpleExpr1.g4  
```
と実行すると、同じディリクトリに  
SimpleExpr1Lexer.py  
SimpleExpr1Parser.py  
SimpleExpr1.tokens  
SimpleExpr1Listener.py  
....  
が生成されます。  

### lexer.py  
 SimpleExpr1Lexer  
SimpleExpr1Lexerは文字列'13+10*7'(正確には Class FileStream) をToken に分割します。  
'10' --> Token [@2,3:4='10',<4>,1:3]   
各数字、文字列の意味は  
`[@tokenIndex, start : stop=text ,&lt;type&gt;, line : column]`  
SimpleExpr1.tokens を開くと   
type は EXPO=1, MULT=2, ADD=3, INT=4, WS=5,'^'=1, '&#42;'=2, '+'=3    
であることが分かります、'10' の type は INT です。

### parser.py  

SimpleExpr1Parser は、  
grammar SimpleExpr1.g4 に従って、  

Token Stream から構文木 (tree) を作ります。  

```
tree:
(stat
   (expr
      (expr 10) +
      (expr
         (expr 123) *
         (expr 3))))
```
