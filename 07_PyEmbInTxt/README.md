

## PyEmbInTxt  

PyEmbInTxt is a tool that runs Python code embedded in text file and replaces it with the output.


- PyEmbInTxt.g4  
```
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
```
Python lexer and parser have been already created  in folder gen.    

If you do not have Python installed,  

download Python3 and `> pip install antlr4-python3-runtime `.  



## example

#### ex1\_text    

```
> python.exe pyEmbInTxt.py ex1_text\example_text.txtpy
This is PyEmbInTxt version 1.0.
PyEmbInTxt creates 'example_text.txt'.
```
example_text.txtpy  
```
///* python.exe pyEmbInTxt.py ex1_text\example_text.txtpy 
This is COMMENT.
*///
example_text \pycode{year=1901/code} ///This is LINE_COMMENT. \pycode{year=2018/code} 

Question: What century is the year \pycode{print(year)/code} in?
Answer  : It is the \pyprn{(year-1)//100 + 1 /prn}th century.
```
"PyEmbInTxt" creates the intermediate file "example_text.py".  
example_text.py  
```
print('#####ctx#####')
print(15)
print('#####ctx#####')
year=1901
print('#####ctx#####')
print(56)
print('#####ctx#####')
print(year)
print('#####ctx#####')
print(84)
print('#####ctx#####')
print((year-1)//100 + 1 )

```

```
> python.exe ex1_text\example_text.py 
#####ctx#####
15
#####ctx#####
#####ctx#####
56
#####ctx#####
1901
#####ctx#####
84
#####ctx#####
20
```
'84' is tokenIndex of Token'\pyprn{(year-1)//100 + 1 /prn}'.   
PyEmbInTxt replaces Token'\pyprn{(year-1)//100 + 1 /prn}'.text with '20'.  

example_text.txt   
```

example_text  

Question: What century is the year 1901 in?
Answer  : It is the 20th century.
```



####  ex2\_latex

`> pip install sympy`  
install pdflatex.exe ( included in [TeX Live](http://www.tug.org/texlive/) , [W32TeX](http://w32tex.org/index.html) )  
```
> python.exe pyEmbInTxt.py ex2_latex\example_latex.texpy
This is PyEmbInTxt version 1.0.
PyEmbInTxt creates 'example_latex.tex'.
> Exit code: 0    Time: 2.024
```


```  
> pdflatex.exe -synctex=1 -interaction=nonstopmode example_latex.tex
```
'pdflatex.exe' creates  example\_latex.pdf   

#### ex3 \_markdown

`> pip install sympy`
```
> python.exe pyEmbInTxt.py ex3_markdown\example_md.pymd
This is PyEmbInTxt version 1.0.
PyEmbInTxt creates 'example_md.md'.
```

#### ex4_math_exercise  
How to make math exercises using PyEmbInTxt and  antlr4_tex2sym.  
`> pip install sympy`  
download  [antlr4_tex2sym](https://github.com/AkiraHakuta/antlr4_tex2sym)  
set antlr4_tex2sym path in math_mod.py.    
install pdflatex.exe ( included in [TeX Live](http://www.tug.org/texlive/) , [W32TeX](http://w32tex.org/index.html) )    

```
> python.exe C:\.....\07_PyEmbInTxt\pyEmbInTxt.py math_exersise.texpy
This is PyEmbInTxt version 1.1.
PyEmbInTxt creates 'math_exersise.tex'.
```

```
> pdflatex.exe -synctex=1 -interaction=nonstopmode math_exersise.tex
```

If you use text editor [SciTE](https://www.scintilla.org/SciTE.html)  , save latexpy.properties in C:\...\wscite363\wscite.   
Set  07_PyEmbInTxt path in  latexpy.properties.   
Add `import latexpy` in SciTEGlobal.properties.  


#### Command  line option

```
> python.exe pyEmbInTxt.py -h
usage: pyEmbInTxt.py [-h] [-v] [-s SEP] filename

positional arguments:
  filename           set filename, for example test.texpy, test.pymd

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      show program's version number and exit
  -s SEP, --sep SEP  set separator, for example -s #$#$MYSEP#$#$
```
### exe file

If you want to convert pyEmbInTxt.py to .exe file ,  
` > pip install cx_Freeze `   
` > python.exe setup.py ` 

```
> PyEmbInTxt\pyEmbInTxt.exe ex2\example_latex.texpy
This is PyEmbInTxt version 1.0.
PyEmbInTxt creates 'example_latex.tex'.
> Exit code: 0    Time: 2.038
```
Even with the exe file, unfortunately there is no difference in execution time.  

### Notes
(1) The Definitive ANTLR 4 Reference (by Terence Parr) eBook, Paper   
(2) [py3antlr4book](https://github.com/jszheng/py3antlr4book)  


### LICENSE

Copyright (c) 2018 Akira Hakuta  
Released under the MIT license  
<https://opensource.org/licenses/mit-license.php>  

### Change log
##### version 1.0 (2018/04/29)

##### version 1.1 (2018/05/13)

- Changed `\pycode{..../code}` to `\begin{pyc}....\end{pyc} (latex style)`
- Changed `\pyprn{...../prn}` to `\pyp{...../pyp}`
- Added   ex4_math_exercise (How to make math exercises using PyEmbInTxt and  antlr4_tex2sym)


*******

###  in japanese    

使用環境 Windows      

- PyEmbInTxt は Python code が埋め込まれた text file から code を抜き取り、  
  その code を実行、code をその出力で置き換えるツールです。  
  構文解析 [ANTLR4](http://www.antlr.org) を使ってそれを実現しています。  　

- lexer, parser, ... は生成済みです。  
  PyEmbInTxt.g4 を変更するのでなければ、Java, antlr-4.7.1-complete.jar は必要ありません。    
  Python が入っていなければ、    
  download [python3](https://www.python.org/downloads/) and `> pip install antlr4-python3-runtime `     

- text file  ex1_text\example_text.txtpy を例として、説明します。  
  ファイル名の拡張子は txt に py を挿入した文字列にして下さい。    
  位置はどこでも構いません。    
  PyEmbInTxt は py を削除したファイル example_text.txt を作ります。   
  `\pycode{....../code}` で囲まれた部分が Python code です。  
  `\pyprn{...../prn}` は `\pycode{print(.....)/code}` と同じです。    

  (1)  grammar PyEmbInTxt.g4  
     `PYCODE : '\\pycode{' .*? '/code}' ;` のように ? がついていると、最短の文字列に    
     `\pycode{year=1901/code} `と`\pycode{print(year)/code}`     
     に match します。  
     ? を取って `\PYCODE : '\\pycode{' .* '/code}' ;`  とすると、最長の文字列   
     `\pycode{year=1901/code} ///This is LINE_COMMENT.....century is the year \pycode{print(year)/code}`  
     に match してしまいます。  
     こんな簡単な文法で Python code を認識することができます。  
     `> antlr4py3 PyEmbInTxt.g4 -o gen`   
     で Python の lexer, parser, ... を gen の中に生成します。  
     既に、生成した lexer, parser, ... がこの folder の中に入っていますので、  
     PyEmbInTxt.g4 を変更するのでなければ、この操作は必要ありません。    

  (2)  `> python.exe pyEmbInTxt.py ex1_text\example_text.txtpy`   
  を実行すると、中間ファイル example_text.py が生成されます。  
  例えば  

     ```
     print('#####ctx#####')
     print(84)
     print('#####ctx#####')
     print((year-1)//100 + 1 )
     ```

     `print((year-1)//100 + 1 )`  は Python のプログラム、   
     `print(84)` の 84 は Token `\pyprn{(year-1)//100 + 1 /prn}` の tokenIndex です。  

     ```
     > python.exe ex1\example_text.py 
     ....
     #####ctx#####
     84
     #####ctx#####
     20
     ```
     この出力の文字列を 区切り文字 '#####ctx#####' (変更可能)で分割し、list を作成、  
     さらに、 dictionary を作り、それを使って、  
     Token `\pyprn{(year-1)//100 + 1 /prn}` の text を '20' に置き換えればよいのですが、  
     ここでは、class  TokenStreamRewriter で Token Stream のコピーを作り、置き換えます。  
     text file example_text.txt  を作って、処理終了！  

- ex2\_latex  
  LaTeX の使用例です。  
    数式処理 SymPy を使っています。  
    関心のない方は、その部分を削除して下さい。  

  **PythonTexとの比較**   
  [PythonTeX](https://github.com/gpoore/pythontex)  ( included in TeX Live , W32TeX )  なるツールがあります。  
    マクロを使うことができます。  
    しかし、3回 compile しなければなりません。  
    test1.tex  
  ```
  \documentclass[pdflatex]{article}

  \usepackage{pythontex}
  \newcommand{\power}[2]{{#1}^{#2}=\py{(#1)**(#2)}}
  \begin{document}
  	{\large\bf test1~~by PythonTeX}\par\vspace{5mm}
  	$\power{2}{20}$\par
  	$\power{3}{30}$
  \end{document}
  ```

   ```
  > pdflatex.exe -synctex=1 -interaction=nonstopmode test1.tex
  > pythontex.exe test1.tex
  > pdflatex.exe -synctex=1 -interaction=nonstopmode test1.tex
   ```


  PyEmbInTxt  では 、マクロが使えないので、   
  test2.texpy  

  ```
  \documentclass[pdflatex]{article}
  \pycode{
  def power(x,y):
  	return str(x)+'^{'+str(y)+'}='+str(x**y)
  /code}
  \begin{document}
  	{\large\bf test2~~by PyEmbInTxt }\par\vspace{5mm}
  	$\pyprn{power(2,20)/prn}$\par
  	$\pyprn{power(3,30)/prn}$
  \end{document}
  ```
  ```
  > python.exe pyEmbInTxt.py ex2_latex\test2.texpy
  > pdflatex.exe -synctex=1 -interaction=nonstopmode test2.tex
  ```
- ex3 \_markdown   
    Markdown の使用例です。  
    数式処理 SymPy を使っています。  
    関心のない方は、その部分を削除して下さい。  
    Markdown には「方言」がいくつかあります。  
    この例は GitHub に従っています。   
    特に、数式の表記に違いがあるようです。  
    他の方言を使う場合は、適宜変更して下さい。  

- ex4_math_exercise
    高校数学演習問題の作成例です。  
     [SciTE](https://www.scintilla.org/SciTE.html) を使うと、かなり快適に使うことができます。  
    (`latexpy.properties`  PDF reader は [Sumatra](https://www.sumatrapdfreader.org/download-free-pdf-viewer.html) を使う設定にしています)     
    答え ( SymPy の出力結果 ) は問題を作る参考、と考えています。  

    `ans = 0` とすると、white で出力、答えが消えます。  


- class  TokenStreamRewriter  
  Python のコードはどうもうまく動きません。  
  Java のコードと比較し、手を加えました。  
  class MyTokenStreamRewriter(TokenStreamRewriter) を作り、  
  def \_reduceToSingleOperationPerIndex(self, rewrites) を override 。  
  class  TokenStreamRewriter については不明な点が多くありますが、  
  元の TokenStream を変更することではないので、安心して使えます。  

- 実行ファイルの作成  
  cx_Freeze を利用すると、exe ファイルを作ることができます。  
  ` > pip install cx_Freeze `   
  ` > python.exe setup.py `   
  フォルダ PyEmbInTxt の中に pyEmbInTxt.exe  ができます。  

  ```
  > PyEmbInTxt\pyEmbInTxt.exe ex2\example_latex.texpy
  This is PyEmbInTxt version 1.0.
  PyEmbInTxt creates 'example_latex.tex'.
  > Exit code: 0    Time: 2.038
  ```
  exe ファイルを使っても、残念ながら、実行時間に差はありません。   

