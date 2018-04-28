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