#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) <= 0:
        return 0
    avg_so_far = responseTimes[0]
    num_greater = 0
    for i in range(1, len(responseTimes)):
        if responseTimes[i] > avg_so_far:
            num_greater += 1
        avg_so_far = (avg_so_far * i + responseTimes[i])/(i+1)
    return num_greater

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
