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
