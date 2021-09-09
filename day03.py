#!/bin/python3

import math
import os
import random
import re
import sys


def is_odd(i):
    return (i % 2) == 1


if __name__ == '__main__':
    N = int(input().strip())

    if is_odd(N):
        print("Weird")
    elif N in range(2, 6) or 20 < N:
        print("Not Weird")
    elif N in range(6, 21):
        print("Weird")




