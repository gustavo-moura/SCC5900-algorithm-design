# -*- coding: utf-8 -*-
"""
# Stable Marriage Problem
## SCC5900 - Algorithm Design

### Lecture 1

#### v1.1
"""
import sys

data = sys.stdin.readlines()
content = [line.rstrip() for line in data]
# with open('1.in', 'r') as file:
#     content = file.readlines()
#     # print(content)

n_test_cases = int(content[0])

test_cases = []
pointer = 1
for i in range(0, n_test_cases):
    n_marriages = int(content[pointer])
    
    pointer += 1
    
    women = []
    for line in range(pointer, pointer + n_marriages):
        woman_data = content[line].split(' ')
        
        preferences = [int(woman_data[wp])-1 for wp in range(1, n_marriages+1)]
    
        women.append(preferences)
        
    pointer += n_marriages
    
    men = []        
    for line in range(pointer, pointer + n_marriages):
        man_data = content[line].split(' ')
        
        preferences = [int(man_data[wp])-1 for wp in range(1, n_marriages+1)]
    
        men.append(preferences)
        

    pointer += n_marriages
    
    case = {
        'n': i,
        'n_marriages': n_marriages,
        'women': women,
        'men': men,
    }
    
    test_cases.append(case)

test_cases

"""## Stable Marriage Algorithm"""

def zeros(n):
    return [0 for i in range(n)]

def nones(n):
    return [None for i in range(n)]

def sequence(l, u):
    return [i for i in range(l, u+l)]

def check(husband, wife):
    for i, m in enumerate(husband):
        if wife[m] == i:
            print('Match')
        else:
            print('Error!')

def inverse_women(women, n):
    inv_women = []
    for woman in women:
        inverse = zeros(n)
        for i in range(0, n):
            inverse[woman[i]] = i

        inv_women.append(inverse)
    return inv_women

def stable_marriage(case):
    women = case['women']
    men = case['men']
    n = case['n_marriages']
    
    inv_women = inverse_women(case['women'], n)
    
    wife = nones(n)
    husband = nones(n)
    freeman = sequence(0, n)

    while len(freeman) != 0:
#         print(f'freeman={freeman}')

        m = freeman[0]    

        man = men[m]

#         print(f'm={m}')
#         print(f'man={man}')

        for w in man:
#             print(f'w={w}')
            m_ = husband[w]
#             print(f'm_={m_}')
            if m_ == None:
                # engage m w
                husband[w] = m
                wife[m] = w
                freeman.pop(0)
#                 print(f'- engages m{m} w{w}')
                break
            else:
#                 print(f'woman {w} preference: m{m}={inv_women[w][m]} and m_{m_}={inv_women[w][m_]}')
                if inv_women[w][m] < inv_women[w][m_]:
                    # engage m w
                    husband[w] = m
                    wife[m] = w
                    freeman.pop(0)
#                     print(f'+ engages m{m} w{w}')

                    # disengage m_ w
                    wife[m_] = None
                    freeman.append(m_)
#                     print(f'--- m_{m_} becomes available')

                    break

#             print('\n')
#         print('\n'*2)
#         print('-'*10)


#     print(f'husband={husband}')
#     print(f'wife={wife}')

#     check(husband, wife)
#     print('Engagements:')
#     for w, m in enumerate(husband):
#         print(f'woman {w + 1} is married to man {m + 1}')

#     print('\n')
    for m, w in enumerate(wife):
#         print(f'man {m + 1} is married to woman {w + 1}')
        print(f'{m + 1} {w + 1}')

"""## Test Case"""

for case in test_cases:
    stable_marriage(case)

