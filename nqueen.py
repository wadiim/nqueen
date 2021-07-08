#!/usr/bin/env python

import sys
import argparse

if sys.version[0] == '2': input = raw_input

# Box drawing characters:
horizontal = u"\u2500"
vertical = u"\u2502"
down_and_right = u"\u250C"
down_and_left = u"\u2510"
up_and_right = u"\u2514"
up_and_left = u"\u2518"
vertical_and_right = u"\u251C"
vertical_and_left = u"\u2524"
horizontal_and_down = u"\u252C"
horizontal_and_up = u"\u2534"
vertical_and_horizontal = u"\u253C"

def is_attacked(x, y, board):
    N = len(board)

    # Check horizontally and vertically
    for i in range(N):
        if board[x][i] == 1: return True
        if board[i][y] == 1: return True

    # Find leftmost cell of the first diagonal
    dx, dy = (0, y + x) if y + x < N else (x - (N - 1 - y), N - 1)
    # Check first diagonal
    while dx < N and dy >= 0:
        if board[dx][dy] == 1: return True
        dx, dy = dx + 1, dy - 1

    # Find leftmost cell of the second diagonal
    dx, dy = (0, y - x) if y - x >= 0 else (x - y, 0)
    # Check second diagonal
    while dx < N and dy < N:
        if board[dx][dy] == 1: return True
        dx, dy = dx + 1, dy + 1

    return False

def solve_n_queen(board, col = 0):
    N = len(board)

    # If all queens has been placed, return True
    if col >= N: return True

    for i in range(N):
        # If this position is attacked, try in the next row
        if is_attacked(i, col, board): continue
        # Otherwise, put the queen here
        board[i][col] = 1
        # Try to place the queens on the other columns
        if solve_n_queen(board, col + 1): return True
        # If that does not lead to a solution, remove the queen
        else: board[i][col] = 0

    return False

def print_board(board):
    print('\n'.join([''.join([str(i) for i in row]) for row in board]))

def pretty_print_row_separator(cols):
    print(''.join(['+---' for i in range(cols)]) + '+')

def pretty_print_row(row, sep, queen_char):
    print(''.join([sep + ' {} '.format(queen_char if i else ' ') for i in row]) + sep)

def pretty_print_horizontal_border_line(n, left, middle, right):
    print(left + (3 * horizontal + middle) * (n - 1) + 3 * horizontal + right)

def pretty_print_board(board, queen_char):
    N = len(board)
    if sys.stdout.encoding.lower() == 'utf-8':
        # Print top horizontal border
        pretty_print_horizontal_border_line(N,
                                            down_and_right,
                                            horizontal_and_down,
                                            down_and_left)
        # Print rows and inner borders under those rows except the last row
        for row in board[:-1]:
            pretty_print_row(row, vertical, queen_char)
            # Print inner horizontal border
            pretty_print_horizontal_border_line(N,
                                                vertical_and_right,
                                                vertical_and_horizontal,
                                                vertical_and_left)
        # Print the last row
        pretty_print_row(board[-1], vertical, queen_char)
        # Print bottom horizontal border
        pretty_print_horizontal_border_line(N,
                                            up_and_right,
                                            horizontal_and_up,
                                            up_and_left)
    else:
        pretty_print_row_separator(N)
        for row in board:
            print(''.join(['| {} '.format(queen_char if i else ' ')
                for i in row]) + '|')
            pretty_print_row_separator(N)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretty", help = 'pretty-print the results',
                        action="store_true")
    parser.add_argument("--queen-char", metavar = 'CHAR',
                        default = 'Q', type = CHAR,
                        help = 'set the character representing the queen')
    return parser.parse_args()

def CHAR(s):
    if len(s) != 1:
        raise ValueError('Not a single character')
    return s

def main():
    args = parse_args()
    try:
        while True:
            n = input()
            board = [[0 for i in range(int(n))] for j in range(int(n))]
            if not solve_n_queen(board):
                print('There is no solution for n =', n)
                continue
            if args.pretty: pretty_print_board(board, args.queen_char)
            else: print_board(board)
    except EOFError:
        pass

if __name__ == '__main__':
	sys.exit(main())
