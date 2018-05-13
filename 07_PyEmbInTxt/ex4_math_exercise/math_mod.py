# set antlr4_tex2sym path
antlr4_tex2sym_Path = r'C:.....\antlr4_tex2sym-master'
import sys
sys.path.append(antlr4_tex2sym_Path)
from antlr4_tex2sym import tex2sym, mylatex


from sympy import *
F=Function('F')
f=Function('f')
var('a:z') 
var('A:DF:HJ:MP:RT:Z')

from enum import Enum,auto

class SymOp(Enum):
    EXPAND = auto()
    FACTOR = auto()
    EQUATION_X = auto()
    INEQUALITY_X = auto()
    EXPAND_TRIG = auto()
    EXPAND_LOG = auto()
    REC_FORM_1 = auto()
    REC_FORM_2 = auto()
    SIMPLIFY = auto()
    RADSIMP = auto()
    SQRTDENEST = auto()
    

import re

replace_list = [['~',''],['\,',''],['\:',''],['\;',''],['\!','']]

def myexpr(expr, symop, ans):
    if ans==1:
        anscolor='\\color{black}'
    else:
        anscolor='\\color{white}'
    expr1 = expr
    for le in replace_list:
        expr1=expr1.replace(le[0],le[1])
    result = '$'+ mylatex_replace(expr)+'$'+'\\par\\myvspace{'+anscolor+ '\\hfill '+'Ans.~$\\displaystyle '
    if symop == SymOp.SIMPLIFY:
        result +=  mylatex(simplify(tex2sym(expr1)))+'$}'
    elif symop == SymOp.EXPAND:
        result +=  mylatex(expand(tex2sym(expr1)))+'$}'
    elif symop == SymOp.FACTOR:
        result +=  mylatex(factor(tex2sym(expr1)))+'$}'
    elif symop == SymOp.RADSIMP:
        result +=  mylatex(radsimp(simplify(tex2sym(expr1))))+'$}'  
    elif symop == SymOp.SQRTDENEST:
        result +=  mylatex(sqrtdenest(tex2sym(expr1)))+'$}'
    elif symop == SymOp.EQUATION_X:
        eq=expand(tex2sym(expr1))
        result +=  mylatex(solve([eq.lhs - eq.rhs] ,[x], domain=S.Complexes ))+'$}' 
    elif symop == SymOp.INEQUALITY_X:
        eq=expand(tex2sym(expr1))
        result +=  mylatex(solve_univariate_inequality(simplify(tex2sym(expr1)), x, relational=False))+'$}'  
    elif symop == SymOp.EXPAND_TRIG:
        result +=  mylatex(expand_trig(tex2sym(expr1)))+'$}'  
    elif symop == SymOp.EXPAND_LOG:
        result +=  mylatex(expand_log(tex2sym(expr1),force=True))+'$}'
    elif symop == SymOp.REC_FORM_1:
        expr_list = re.split(',', expr1)
        if len(expr_list) != 2:
            result='error!'
        else:
            eq=expand(tex2sym(expr_list[0]))
            a1=expand(tex2sym((expr_list[1]).replace(' ','').replace('a_1=','')))
            result_expr = mylatex(rsolve(eq,F(n), {F(1):a1}))
            result +=  'a_n=' + result_expr+'$}'
    elif symop == SymOp.REC_FORM_2:        
        expr_list = re.split(',', expr1)
        if len(expr_list) != 3:
            result='error!'
        else:
            eq=expand(tex2sym(expr_list[0]))
            a1=expand(tex2sym((expr_list[1]).replace(' ','').replace('a_1=','')))
            a2=expand(tex2sym((expr_list[2]).replace(' ','').replace('a_2=','')))
            result_expr = mylatex(rsolve(eq,F(n), {F(1):a1,F(2):a2}))
            result +=  'a_n=' + result_expr+'$}'
    return result 

def mylatex_replace(expr):
    replace_list=[['\\ii',' i'],['\\ee',' e'],['\\ppi','\\pi '],['\\C','\\mathrm{C}'],['\\P','\\mathrm{P}'],['\\ln','\\log']
                ,['\\sum','\\displaystyle\sum '],['\\lim','\\displaystyle\lim '],['\\int','{\\displaystyle\int}']]
    result=expr
    for le in replace_list:
        result=result.replace(le[0],le[1])
    return result
    
