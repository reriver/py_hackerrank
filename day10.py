#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    s = "{0:b}".format(n)
    ones = "{0:b}".format(n).count('1')
    for i in range(ones, 0, -1):
        if s.count('1' * i) > 0:
            print(i)
            exit()

