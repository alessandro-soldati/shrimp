import sys
import argparse
import rpncalc

TEST_REAL = '2 3*5+ 1+ 3/'
TEST_TRIG = 'pi 2 / sin'
TEST_OPTS = '--stack-view 10 ' + TEST_REAL
TEST_STRING = '0x47 2e3 1.3e17 pi \t -1.2e-1 0xAf7 0o777 0b1101 -0B101 4 5+e*/ atan2 2,7 asdf -3.14E+6.7'
PROG_NAME = 'Shrimp'
VERSION = (0, 1, 0)

if __name__ == "__main__":
    
    version_string = PROG_NAME + ' ' + '.'.join(str(num) for num in VERSION)
    parser = argparse.ArgumentParser(
        description="Reverse Polish Notation (RPN) calculator with advanced functions.")
    parser.add_argument('commands', nargs='*', default='',
        help="commands to be directly fed to the calculator")
    parser.add_argument('-s', '--stack-view', default=5,
        help="stack depth to see in the calculator")
    parser.add_argument('-a', '--angle-view', default='rad', choices=['deg', 'rad', 'grad'],
        help="angle unit for viewing")
    parser.add_argument('-c', '--complex-view', default='cart', choices=['cart', 'pol'],
        help="viewing form for complex numbers")
    parser.add_argument('-p', '--program',
        help="filename containing the program to run")
    parser.add_argument('-v', '--verbose', action='count', default=0,
        help="turn on internal information visualization")
    parser.add_argument('--version', action='version', version=version_string)
    args = parser.parse_args()
    print(args)
    
    print("SHRIMP - RPN calculator")
    calc = rpncalc.RPNcalc()
    
    for arg in args.commands:
        calc.proc(arg)
        stack = calc.get_stack(args.stack_view)
        print(stack)
    
    for line in sys.stdin:
        if line.strip() == 'exit':
            sys.exit()
        calc.proc(line)
        stack = calc.get_stack(args.stack_view)
        print(stack)
