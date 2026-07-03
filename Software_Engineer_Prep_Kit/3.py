#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # Write your code here
    new_string = ""
    for letter in code:
        if (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) <= 122 and ord(letter) >= 97):
            new_string = new_string + letter
    
    new_string = new_string.lower()
    return new_string == ''.join(reversed(new_string))    

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
