#!/usr/bin/python

import sys
from collections import defaultdict

sys.setrecursionlimit(1000001)

amounts = [1, 5, 10, 25, 50]


def making_change(amount, denominations):

    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif len(denominations) == 0:
        return 0
    else:
        return making_change(amount - denominations[0], denominations) + making_change(amount, denominations[1:])


# print(making_change(1, amounts))
# print(making_change(5, amounts))

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
