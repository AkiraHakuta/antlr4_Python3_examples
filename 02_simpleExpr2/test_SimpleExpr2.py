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