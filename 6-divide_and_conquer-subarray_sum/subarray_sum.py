# -*- coding: utf-8 -*-
"""
# Backtracking Algorithm
## SCC5900 - Algorithm Design

### Lecture 6

#### v1

$ python subarray_sum.py < 1.in > 1_ans.out
"""
import sys

INF_NEG = -99999

def max_subarray_sum(arr):
    n = len(arr)

    if n==1:
        return arr[0]

    m = int(n/2)
    
    left_mss = max_subarray_sum(arr[:m])
    right_mss = max_subarray_sum(arr[m:n])

    left_sum = INF_NEG
    right_sum = INF_NEG

    sum = 0
    for i in range(m, n):
        sum += arr[i]
        right_sum = max(right_sum, sum)

    sum = 0
    for i in range(m-1, -1, -1):
        sum += arr[i]
        left_sum = max(left_sum, sum)

    ans = max(left_mss, right_mss)
    return max(ans, left_sum + right_sum)



data = sys.stdin.readlines()
content = [line.rstrip() for line in data]

n_cases = int(content[0])

for i_case in range(n_cases):

    pointer = i_case * 2

    pointer += 1
    array_size = int(content[pointer])

    pointer += 1
    arr = [int(n) for n in content[pointer].split(' ')]
    # print(arr)

    ans = max_subarray_sum(arr)

    print(f'Soma maxima = {ans}')
