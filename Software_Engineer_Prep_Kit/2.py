#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    
    # idea: loop through all the indices in the array
    #   look at first number (x) in array
    #   see what index it should be at (x-1)
    #   swap those two numbers
    # look at the new number in the current index
    # if its not in the right place, repeat
    # if it is in the right place, move on to the next index
    # also move on if the number is negative or both numbers being analyzed are duplicates or its greater than n
    for i in range(len(orderNumbers)):
        while orderNumbers[i] != i+1 and orderNumbers[i] > 0 and orderNumbers[i] <= len(orderNumbers) and orderNumbers[i] != orderNumbers[orderNumbers[i] - 1]:
            temp = orderNumbers[orderNumbers[i] - 1]
            orderNumbers[orderNumbers[i] - 1] = orderNumbers[i]
            orderNumbers[i] = temp
    
    # array pass through
    num_to_find = 1
    for num in orderNumbers:
        if num > num_to_find:
            return num_to_find
        else:
            if num == num_to_find:
                num_to_find += 1
    return num_to_find

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
