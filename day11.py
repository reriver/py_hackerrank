#!/bin/python3

import math
import os
import random
import re
import sys


def hourglass(a, y, x):
    if x <= 0 or 6 <= x or y <= 0 or 6 <= x:
        return -1
    h = a[y-1][x-1] + a[y-1][x] + a[y-1][x+1]
    h += a[y][x]
    h += a[y+1][x-1] + a[y+1][x] + a[y+1][x+1]
    return h


if __name__ == '__main__':

    arr = []

    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        print(arr[i])
    # print(arr)
    # print(hourglass(arr, 4, 3))
    # print(hourglass(arr, 2, 1))

    hs = [[0 for x in range(6-2)] for y in range(6-2)]
    for y in range(1, 5, 1):
        for x in range(1, 5, 1):
            hs[y-1][x-1] = hourglass(arr, y, x)
        # print(hs[y-1])
    # print(hs)
    print(max(map(max, hs)))

