#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples_on_house = 0
    oranges_on_house = 0
    arr_of_apples_oranges_on_house = []
    apples_arr_plus_dist_a = 0
    oranges_arr_plus_dist_b = 0

    #loop through apples array and oranges array and sum their respective distances
    apples_arr_plus_dist_a = [apple + a for apple in apples]
    oranges_arr_plus_dist_b = [orange + b for orange in oranges]

    #within range of s and t inclusive
    #count how many apples / oranges fall into range
    #add apples and oranges that fell on house to array
    tmp_apples_on_house = [apples_on_house + 1 for x in apples_arr_plus_dist_a if x in range(s, t + 1)]
    tmp_oranges_on_house = [oranges_on_house + 1 for y in oranges_arr_plus_dist_b if y in range(s, t + 1)]
    for x in tmp_apples_on_house:
        apples_on_house += x
    for y in tmp_oranges_on_house:
        oranges_on_house += y
    arr_of_apples_oranges_on_house.append(apples_on_house)
    arr_of_apples_oranges_on_house.append(oranges_on_house)

    #print apple int and orange int
    [print(x) for x in arr_of_apples_oranges_on_house]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
