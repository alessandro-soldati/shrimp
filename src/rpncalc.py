# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:10:13 2022

@author: alex8
"""

import re
import numbers
import math

# Class definition, inherits from standard lists
class RPNcalc(list):
    
    PARSE_DICT_DEFAULT = {
        'int_hex': (r'[\+\-]?0[xX][0-9a-fA-F]+', lambda x: int(x, 16)), # base 16, integer only
        'int_oct': (r'[\+\-]?0[oO][0-7]+', lambda x: int(x, 8)), # base 8, integer only
        'int_bin': (r'[\+\-]?0[bB][01]+', lambda x: int(x, 2)), # base 2, integer only
        'number' : (r'[\+\-]?\d+(?:\.\d+)?(?:[eE][\+\-]?\d+)?', lambda x: float(x)), # base 10, possibly exp notation
        'oper'   : (r'[\+\-\*/]', lambda x: str(x)), # common operators
        'func'   : (r'\w+', lambda x: str(x)), # remaining functions
        'error'  : (r'\S+', lambda x: None) # all the rest is error, unless whitespace
        }
    
    FUNC_DICT_DEFAULT = {
        # common operators
        '+': (2, lambda x, y: y + x),
        '-': (2, lambda x, y: y - x),
        '*': (2, lambda x, y: y * x),
        '/': (2, lambda x, y: y / x),
        # stack manipulation
        'swap': (2, lambda x, y: (x, y)),
        'pop': (1, lambda x: None),
        'dup': (1, lambda x: (x, x)),
        # power
        'pow': (2, lambda x, y: y**x),
        'sqrt': (1, math.sqrt),
        'root': (2, lambda x, y: y**(1/x)), # Python 3 only!
        # trigonometric functions
        'sin': (1, math.sin),
        'cos': (1, math.cos),
        'tan': (1, math.tan),
        'asin': (1, math.asin),
        'acos': (1, math.acos),
        'atan': (1, math.atan),
        'atan2': (2, math.atan2),
        # transcendental functions
        'exp': (1, math.exp),
        'ln': (1, math.log),
        'log': (1, math.log10),
        # constants
        'pi': (0, lambda: math.pi),
        'e': (0, lambda: math.exp(1))
        }
    
    def __init__(self):
        list.__init__(self)
        self.parse_dict = RPNcalc.PARSE_DICT_DEFAULT
        self.func_dict = RPNcalc.FUNC_DICT_DEFAULT
        self.all_regex = '|'.join('(?P<%s>%s)' % 
                                  (key, val[0]) for key, val in self.parse_dict.items())
        
    def proc(self, data):
        for tok in re.finditer(self.all_regex, data):
            value, tok_type = tok.group(0), tok.lastgroup
            value = self.parse_dict[tok_type][1](value)
            if isinstance(value, numbers.Number): # numbers are pushed on the stack
                self.append(value)
            elif tok_type == 'oper' or tok_type == 'func': # functions are processed
                if value in self.func_dict:
                    num_args, func = self.func_dict[value]
                    args = []
                    for cnt in range(num_args):
                        args.append(self.pop())
                    res = func(*args)
                    if res == None:
                        pass
                    elif isinstance(res, tuple): # TODO improve with a unique statement
                        self.extend(res)
                    else:
                        self.append(res)
            else:
                print('Error!')
     