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
        
        
file_name = 'test3.expr'
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