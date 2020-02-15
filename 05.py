"""2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?"""

from typing import List
from numpy import prod
from utilities import find_primes, highest_power

N: int = 20

# First find all primes smaller than N

primes = find_primes(N)

# Then find all powers of those primes that are smaller than N

powers_of_primes = [highest_power(prime, N) for prime in primes]

if __name__ == "__main__":
    
    solution = prod(powers_of_primes)
    print(solution)