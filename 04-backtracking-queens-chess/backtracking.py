# -*- coding: utf-8 -*-
"""
# Backtracking
## SCC5900 - Algorithm Design

### Lecture 4

#### v1
"""
import sys


def printBoard(board):
    for l in range(8):
        for c in range(8):
            print(f"{board[l][c]:2}", end=" ")
        print('')


def zeroes(l):
    return [False for _ in range(l)]


def condition(lin, col, params):
    if (
        not params['lines'][lin]
        and not params['right_diagonal'][lin - col + 7] 
        and not params['left_diagonal'][lin + col]
    ):
        return True
    return False
        

def set_control(lin, col, params, boolean):
    params['lines'][lin] = boolean
    params['right_diagonal'][lin - col + 7] = boolean
    params['left_diagonal'][lin + col ] = boolean
    

def backtracking(col, summ, params, max_scores):
    if col == 8:
        max_scores.append(summ)
        return True

    for lin in range(8):
        if condition(lin, col, params):
            set_control(lin, col, params, True)

            backtracking(col + 1, summ + params['board'][lin][col], params, max_scores)

            set_control(lin, col, params, False)
            
    return False


def solveQueens(board):
    max_scores = []
    
    # Control lists, marks if a queen blocks certain line or diagonal
    params = {
        'lines': zeroes(8), # lines
        'right_diagonal': zeroes(15), # diagonals left-up to right-down
        'left_diagonal': zeroes(15), # diagonals right-up to left-down
        'board': board,
    }
    
    backtracking(0, 0, params, max_scores)

    print(f"{max(max_scores):5}")


if __name__ == "__main__":

    # with open('1.in', 'r') as file:
    #     content = file.readlines()

    data = sys.stdin.readlines()
    content = [line.rstrip() for line in data]

    n_test_cases = int(content[0])

    # boards = []
    for n in range(0, n_test_cases):
        board = []
        for l in range(1,9): # Board square with size 8
            line = [int(c) for c in content[n * 8 + l].replace('\n', '').split()]
            board.append(line)

        solveQueens(board)
            
        # boards.append(board)







