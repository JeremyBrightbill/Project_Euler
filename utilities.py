"""Utility functions for use in multiple programs"""

from typing import List

# Find all primes up to a given limit using Sieve of Eratosthenes 
# (https://www.geeksforgeeks.org/sieve-of-eratosthenes/) 

def find_primes(n): 
    # Start by marking all numbers in range as True
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n): 
        if prime[p] == True: 
            # Mark multiples as False
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    output = [p for p in range(2, n) if prime[p]]
    return output

# Find the highest power a number less than or equal to given limit: 

def highest_power(n: int, limit: int) -> int:
    exponent: int = 1
    while True: 
        next_exponent = exponent + 1
        if n ** next_exponent <= limit:
            exponent = next_exponent
            continue
        else:
            output = n ** exponent
            break
    return output