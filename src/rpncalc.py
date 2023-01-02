# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:10:13 2022

@author: alex8
"""

import re
import numbers
import math

# Class definition
class RPNcalc:
    def __init__(self):
        self.stack = []
        
    def load(self, data):
        PARSE_DICT = {
            'int_hex': (r'[\+\-]?0[xX][0-9a-fA-F]+', lambda x: int(x, 16)), # base 16, integer only
            'int_oct': (r'[\+\-]?0[oO][0-7]+', lambda x: int(x, 8)), # base 8, integer only
            'int_bin': (r'[\+\-]?0[bB][01]+', lambda x: int(x, 2)), # base 2, integer only
            'number' : (r'[\+\-]?\d+(?:\.\d+)?(?:[eE][\+\-]?\d+)?', lambda x: float(x)), # base 10, possibly exp notation
            'oper'   : (r'[\+\-\*/]', lambda x: str(x)), # common operators
            'func'   : (r'\w+', lambda x: str(x)), # remaining functions
            'error'  : (r'\S+', lambda x: None) # all the rest is error, unless whitespace
            }
        FUNC_DICT = {
            '+': (2, lambda x, y: y + x),
            '-': (2, lambda x, y: y - x),
            '*': (2, lambda x, y: y * x),
            '/': (2, lambda x, y: y / x),
            'sin': (1, math.sin),
            'pi': (0, math.pi)
            }
        all_regex = '|'.join('(?P<%s>%s)' % (key, val[0]) for key, val in PARSE_DICT.items())
        for tok in re.finditer(all_regex, data):
            value, tok_type = tok.group(0), tok.lastgroup
            print('%10s: %10s' % (value, tok_type))
            value = PARSE_DICT[tok_type][1](value)
            if isinstance(value, numbers.Number):
                self.stack.append(value)
            elif tok_type == 'oper' or tok_type == 'func':
                if value in FUNC_DICT:
                    num_args, func = FUNC_DICT[value]
                    args = []
                    for cnt in range(num_args):
                        args.append(self.stack.pop())
                    if num_args > 0:
                        self.stack.append(func(*args))
                    else:
                        self.stack.append(func) # not a real function, just a constant
                    print(f'operands {num_args}:{args}')
            else:
                print('Error!')
        
    def get(self):
        return self.stack.pop()
        
    def get_all(self):
        return self.stack
