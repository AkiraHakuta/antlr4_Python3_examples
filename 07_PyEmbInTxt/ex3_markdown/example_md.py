print('#####ctx#####')
print(121)
print('#####ctx#####')

import math

def md_mathexpr(expr):
    expr1 = expr.replace('\\int ', '{\\int}')
    expr1 = expr1.replace(' ', '')
    return '<img src="https://latex.codecogs.com/gif.latex?' + expr1 + '" />' # for GitHub (Atom editor)
    #return '$$' + '\\displaystyle ' + expr1 + '$$'# Python comment
    #return '[tex:{' + '\\displaystyle ' + expr1 + '}]'

start, end ,step= 0.0, 90.0, 5.0
deg = start
while True:    
    rad = deg * math.pi /180
    if deg > 89.999:
        print('|{:2.1f}|{:8.7f}|{:8.7f}| undefined |'.format(deg, math.sin(rad), math.cos(rad)))
    else:
        if math.tan(rad) < 10:
            print('|{:2.1f}|{:8.7f}|{:8.7f}|{:8.7f}|'.format(deg, math.sin(rad), math.cos(rad), math.tan(rad)))
        else:
            print('|{:2.1f}|{:8.7f}|{:8.7f}|{:7.3e}|'.format(deg, math.sin(rad), math.cos(rad), math.tan(rad)))
    deg += step
    if deg > 90.000:
        break        

print('#####ctx#####')
print(209)
print('#####ctx#####')

from sympy import *
x = symbols('x')
func_list = [x**2*sin(x), x**2*exp(x), x**2*log(x)]
for func in func_list:
    math_str = '|'
    math_str += md_mathexpr(latex(Derivative(func, x))+'='+latex(Derivative(func, x).doit()))
    math_str += '|'
    math_str +=  md_mathexpr(latex(Integral(func, x))+'='+latex(Integral(func, x).doit())+'+C')
    math_str += '|'
    print(math_str)

print('#####ctx#####')
print(273)
print('#####ctx#####')
print('antlr4はLL構文解析に基づくparser generatorである')
print('#####ctx#####')
print(280)
print('#####ctx#####')

num = 10
print('\'日本語 \'を',num,'回表示します  ')
for i in range(num):
    print('日本語 ',end='')

