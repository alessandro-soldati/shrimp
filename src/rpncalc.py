# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:10:13 2022

@author: alex8
"""

import re

# Class definition
class RPNcalc:
    def __init__(self):
        self.stack = []
        
    def proc_error(value):
        print('Parsing error')
        return None
    
    def proc_pass(value):
        return value
    
    def load(self, data):
        PARSE_DICT = {
            'int_hex': (r'0[xX][0-9a-fA-F]+', RPNcalc.proc_pass), # base 16, integer only
            'int_oct': (r'0[oO][0-7]+', RPNcalc.proc_pass), # base 8, integer only
            'int_bin': (r'0[bB][01]+', RPNcalc.proc_pass), # base 2, integer only
            'number' : (r'-?\d+(?:\.\d+)?(?:[eE]-?\d)?', RPNcalc.proc_pass), # base 10, possibly exp notation
            'oper'   : (r'[\+\-\*/]', RPNcalc.proc_pass), # common operators
            'func'   : (r'\w+', RPNcalc.proc_pass), # remaining functions
            'error'  : (r'\S+', RPNcalc.proc_error) # all the rest is error
            }

        all_regex = '|'.join('(?P<%s>%s)' % (key, val[0]) for key, val in PARSE_DICT.items())
        for tok in re.finditer(all_regex, data):
            value, tok_type = tok.group(0), tok.lastgroup
            print('%10s: %10s' % (value, tok_type))
            self.stack.append(PARSE_DICT[tok_type][1](value))
        
    def get(self):
        return self.stack.pop()
        
    def all(self):
        return self.stack
