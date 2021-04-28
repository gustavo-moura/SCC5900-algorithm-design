# -*- coding: utf-8 -*-
"""
# Greedy Algorithm
## SCC5900 - Algorithm Design

### Lecture 3

#### v1

## Read File
"""
import sys

data = sys.stdin.readlines()
content = [line.rstrip() for line in data]

test_cases = []

i = 0
while True:
    bs = content[i].split(' ')
    b = int(bs[0])
    s = int(bs[1])

    if b==0 and s==0:
        break

    i += 1

    b_ages = []
    for i_b in range(i, i+b):
        b_ages.append(int(content[i_b]))

    i += b

    s_ages = []
    for i_s in range(i, i+s):
        s_ages.append(int(content[i_s]))

    i += s

    test_cases.append({
        "b": b,
        "s": s,
        "b_ages": b_ages,
        "s_ages": s_ages
    })

"""## Greedy - Bus Drivers"""

def greedy(case):
    b = case['b']
    s = case['s']
    b_ages = case['b_ages']
    # s_ages = case['s_ages']

    # Exploiting the system | The greedy here is me
    if (b-s) <= 0:
        print(0)
    else:
        # Sort lists
        b_ages.sort()
        
        print(f'{b-s} {b_ages[0]}')
    

"""## Test Case"""

for i, case in enumerate(test_cases):
    print(f'Case {i+1}: ', end='')
    greedy(case)

