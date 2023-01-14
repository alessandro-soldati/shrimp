# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 20:46:41 2023

@author: alex8
"""

import sys
import getopt
import argparse

# Show all arguments
n = len(sys.argv)
print(f"Found {n} argument{'s' if n > 1 else ''}:")
ii = 0
for arg in sys.argv:
    print(f"{ii:4d}: {arg}")
    ii = ii + 1

# GNU getopt parsing
opts, args = getopt.gnu_getopt(sys.argv[1:], "hvs:", ["help", "version", "stack-len="])
print(opts)
print(args)

# argparse parsing
parser = argparse.ArgumentParser(
    prog="SHRIMP",
    description="Reverse Polish Notation (RPN) calculator with advanced functions.",
    epilog="(c) A. Soldati, 2023")
parser.parse_args()
