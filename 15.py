"""Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Algorithm: It's the number of permutations of SIDE + SIDE, divided by 
(2 * permutations of SIDE)."""

from math import factorial

SIDE: int = 20

if __name__ == "__main__":
    result = factorial(SIDE + SIDE) / (2 * factorial(SIDE))
    print(result)