from antlr4 import *

from gen.PyEmbInTxtLexer import PyEmbInTxtLexer
from gen.PyEmbInTxtParser import PyEmbInTxtParser
from gen.PyEmbInTxtListener import PyEmbInTxtListener
from MyTokenStreamRewriter import MyTokenStreamRewriter
from Interval import Interval

DEFAULT_PROGRAM_NAME = MyTokenStreamRewriter.DEFAULT_PROGRAM_NAME

import os
import subprocess
import argparse
import re

version = '1.1'
DEFAULT_SEP = '#####ctx#####'

# PYCODE : '\\begin{pyc}' .*? '\\end{pyc}' ;
# PYPRN  : '\\pyp{' .*? '/pyp}'  ;
PYCODE_left_len = len('\\begin{pyc}')
PYCODE_right_len = len('\\end{pyc}')
PYPRN_left_len = len('\\pyp{')
PYPRN_right_len = len('/pyp}')

class ExtractPyCode(PyEmbInTxtListener):
    def __init__(self, sep):
        super().__init__()
        self.sep = sep
        self.pycode = ''
    
    def enterPyc(self, ctx):
        startIndex = ctx.start.tokenIndex
        ctx_getText = ctx.getText()[PYCODE_left_len: -PYCODE_right_len:]
        pycode = "print(\'" + self.sep + "\')\n" + "print(" + str(startIndex) + ")\n"+ "print(\'" + self.sep + "\')\n" + ctx_getText + "\n"
        self.pycode += pycode       
        
    def enterPyp(self, ctx):
        startIndex = ctx.start.tokenIndex
        ctx_getText = ctx.getText()[PYPRN_left_len: -PYPRN_right_len:]
        pycode = "print(\'" + self.sep + "\')\n" + "print(" + str(startIndex) + ")\n"+ "print(\'" + self.sep + "\')\n" + "print(" + ctx_getText + ')\n'
        self.pycode += pycode
        

def cut_CPLF(strg):
    result = strg
    if len(result) < 2: return result
    if result[:2] == '\r\n':
        result = result[2:]
    if len(result) < 2: return result
    if result[-2:] == '\r\n':
        result = result[:-2]
    return result        
    

def run_python(filename, sep):    
    python_cmd= 'python.exe '+ filename
    try:
        #result = subprocess.check_output(python_cmd)
        result = subprocess.run(python_cmd, stdout=subprocess.PIPE).stdout.decode('cp932')
    except:
        print('subprocess.run error!')
        return 1  
    result_list = re.split(sep, result)
    result_num = len(result_list)
    result_dic ={}
    for i in range((result_num-1)//2):
        if result_list[2*i+2] == '\r\n':
            value = ''
        else:
            value = cut_CPLF(result_list[2*i+2])
        result_dic[int(result_list[2*i+1][2:-2:])] = value
    
    return result_dic    
    
           
def main(file_name, sep, file_list):    
    path = file_list[0]
    sf_ext = file_list[1]
    file_name = path + sf_ext
    try:
        input_stream = FileStream(file_name, encoding='utf-8')
    except OSError:
        print('cannot open', file_name)
        quit()
    lexer = PyEmbInTxtLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    #print('tokens:')
    #for tk in token_stream.tokens:
    #    print(tk)
    parser = PyEmbInTxtParser(token_stream)
    tree = parser.stat()
    lisp_tree_str = tree.toStringTree(recog=parser)

    walker = ParseTreeWalker()
    epc = ExtractPyCode(sep)    
    walker.walk(epc, tree)
    pyfile = path + '.py'
    f = open(pyfile, 'w', encoding='utf-8')
    f.write(epc.pycode.replace('\r\n','\n'))
    f.close()
    result_dic = run_python(pyfile, sep)

    rewriter = MyTokenStreamRewriter(token_stream)
    for i in result_dic.keys():      
        rewriter.replaceIndex(i, result_dic[int(i)])        
    interval = Interval(rewriter.tokens.tokens)
    result =rewriter.getText(DEFAULT_PROGRAM_NAME,interval).replace('\r\n','\n')
    ext = sf_ext[1:].replace('py','')
    create_file = path + '.' + ext
    f = open(create_file,'w', encoding='utf-8')
    f.write(result)
    f.close()

    print('PyEmbInTxt creates \'{}\'.'.format(os.path.basename(create_file)))



if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument("filename", help="set filename, for example test.texpy, test.pymd")    
    aparser.add_argument('-v','--version', version='%(prog)s version {}'.format(version), action='version')
    aparser.add_argument("-s","--sep", help="set separator, for example -s #$#$MYSEP#$#$",default = DEFAULT_SEP)
    args = aparser.parse_args()
    print('This is PyEmbInTxt version {}.'.format(version))
    filename = args.filename
    path, sf_ext = os.path.splitext(filename)
    if sf_ext[1:].find('py') == -1 or sf_ext[1:].replace('py','') == '':
        print('extension error')
        quit()
    main(filename, args.sep, [path, sf_ext])
