# -*- coding: utf-8 -*-
"""
# Backtracking Algorithm
## SCC5900 - Algorithm Design

### Lecture 5

#### v1

$ python backtracking.py < 1.in > 1_ans.out
"""
import sys
from itertools import product

def get_passwords_from_rule(words, rule):

    digits = [str(i) for i in range(10)]

    par = []
    for char in rule:
        if char == '#':
            par.append(words)
        if char == '0':
            par.append(digits)

    passwords = []
    for t in product(*par):
        passwords.append(''.join(t))

    return passwords


def get_passwords(words, rules):

    passwords = []
    for rule in rules:
        passwords_aux = get_passwords_from_rule(words, rule)
        passwords.extend(passwords_aux)

    return passwords


data = sys.stdin.readlines()
content = [line.rstrip() for line in data]

line = 0

while line < len(content):

    n_words = int(content[line])
    # print(f"{n_words=}")

    line += 1

    words = []
    for i in range(line, line + n_words):
        word = content[i]
        words.append(word)
    
    # print(words)

    line += n_words

    n_rules = int(content[line])
    # print(f"{n_rules=}")

    line += 1

    rules = []
    for i in range(line, line + n_rules):
        rule = content[i]
        rules.append(rule)

    # print(rules)

    line += n_rules

    passwords = get_passwords(words, rules)

    print('--')
    for p in passwords:
        print(p)
