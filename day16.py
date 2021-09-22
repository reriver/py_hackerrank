#!/bin/python3

import sys

S = input()
try:
    x = int(S)
except ValueError:
    print("Bad String")
else:
    print(x)

