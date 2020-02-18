"""Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

from utilities import pythagorean

N: int = 1000

if __name__ == "__main__": 

    print(pythagorean(N))