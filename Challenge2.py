#!/usr/bin/python3

import sys
arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])
arg3 = float(sys.argv[3])
print(str(arg1 + arg2) + " " + str(arg1 * arg3) + " " + str(arg1 % arg2) + " " + str(arg3 // arg1))
arg1 = (arg1 + 1)
arg2 = (arg2 + 1)
arg3 = (arg3 + 1)
print(str(arg1 >> 3) + " " + str(arg2 / 2) + " " + str(arg1 | arg2))
print(arg1 + (len(sys.argv) -1))
