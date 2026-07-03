#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def isNonTrivialRotation(s1, s2):
    # idea: locate the first instance of the s1[0] in s2. if it doesnt exist, false.
    # then, walk along the indices in order, confirming they are all the same.
    # if one is ever wrong, false.
    # if index of s2 is >= len(s2), index in s2 wraps back to zero
    try:
        s2_idx = s2.index(s1[0])
    except ValueError:
        return False
    if s2_idx == 0:
        return False
    for i in range(len(s1)):
        if s1[i] != s2[s2_idx]:
            return False
        s2_idx += 1
        if s2_idx == len(s2):
            s2_idx = 0
    return True

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))
