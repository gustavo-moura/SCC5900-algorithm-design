# -*- coding: utf-8 -*-
"""
# Greedy Algorithm
## SCC5900 - Algorithm Design

### Lecture 2

#### v1

## Read File
"""
import sys

data = sys.stdin.readlines()
content = [line.rstrip() for line in data]

test_cases = []

i = 0
while True:
    ndr = content[i].split(' ')
    n = int(ndr[0])
    d = int(ndr[1])
    r = int(ndr[2])

    if n==0 and d==0 and r==0:
        break

    i += 1
    len_morning = [int(len) for len in content[i].split(' ')]

    i += 1
    len_evening = [int(len) for len in content[i].split(' ')]

    test_cases.append({
        "n": n,
        "d": d,
        "r": r,
        "len_morning": len_morning,
        "len_evening": len_evening
    })

    i += 1

# print(test_cases)

"""## Greedy - Bus Drivers"""

def greedy(case):
    n = case['n']
    d = case['d']
    r = case['r']
    len_morning = case['len_morning']
    len_evening = case['len_evening']

    # Sort lists
    len_morning.sort()
    len_evening.sort(reverse=True)

    cumulative = 0
    for i in range(n):
        working_hours = len_morning[i] + len_evening[i]
        exceding_hours = working_hours - d
        if exceding_hours > 0:
            cumulative += exceding_hours

    overtime_pay = cumulative * r

    print(overtime_pay)

"""## Test Case"""

for case in test_cases:
    greedy(case)

