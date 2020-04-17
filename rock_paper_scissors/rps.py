#!/usr/bin/python

import sys

# n = number of players
# inner recursion =>


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    results = []

    def combination(n, com=[]):
        if n == 0:
            results.append(com)
            return

        for choice in options:
            combination(n - 1, com + [choice])

    combination(n, [])

    return results


# print(rock_paper_scissors(1))
# print(rock_paper_scissors(2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
