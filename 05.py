"""Smallest multiple

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?"""

from typing import List
from numpy import prod
from utilities import find_primes, highest_power

N: int = 20

if __name__ == "__main__":
    
    # First find all primes smaller than N
    primes = find_primes(N)

    # Then find the highest powers of those primes that are smaller than N
    powers_of_primes = [highest_power(prime, N) for prime in primes]

    # The product of those numbers will be the smallest number evenly 
    # divisible by all
    solution = prod(powers_of_primes)
    print(solution)