#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)-1):
        sum1 = sum1 + arr[i]
    for j in range(1, len(arr)):
        sum2 = sum2 + arr[j]
    print(sum1, end=" ")
    print(sum2)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
