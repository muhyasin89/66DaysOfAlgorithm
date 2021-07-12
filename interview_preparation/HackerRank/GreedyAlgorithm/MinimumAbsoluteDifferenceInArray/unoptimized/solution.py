#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def minimumAbsoluteDifference(arr):
    # Write your code here
    min_abs = min((abs(arr[i] - arr[i - 1]) for i in range(1, len(arr))))
    s = set()
    for x in arr:
        if x in s:
            return 0
        for d in range(1, min_abs):
            if x + d in s or x - d in s:
                min_abs = d
                break
        s.add(x)
    return min_abs


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
bn
