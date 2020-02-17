"""Utility functions for use in multiple programs"""

from typing import List


# For Exercise 3

def find_prime_factors(n: int) -> List[int]: 
    """Prime factorization by trial division"""
    output: List[int] = []
    factor: int = 2
    while factor <= n:
        if n % factor == 0: 
            output.append(factor)
            n = n / factor
        else: 
            factor += 1
    return output


# For Exercise 5

def find_primes(n: int) -> List: 
    """Find all primes up to a given limit using Sieve of Eratosthenes 
(https://www.geeksforgeeks.org/sieve-of-eratosthenes/)"""
    
    # Start by marking all numbers in range as True
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n): 
        if prime[p] == True: 
            # Mark multiples as False
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    output: List[int] = [p for p in range(2, n) if prime[p]]
    return output
 

def highest_power(n: int, limit: int) -> int:
    """Find the highest power a number less than or equal to given limit"""
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


# For Exercise 7

def is_prime(n: int) -> bool: 
    """Determine if a given number is prime"""
    root = n**0.5
    factor: int = 2
    if n < 2: 
        return False
    while factor <= root: 
        if n % factor == 0: 
            return False
        else:
            factor += 1
    return True

def find_n_primes(n: int) -> List:
    """Find the nth prime number"""
    number: int = 2
    primes: List[int] = []

    while len(primes) < n: 
        if is_prime(number): 
            primes.append(number)
        number += 1

    return primes[-1]

# For Exercise 9

def pythagorean(n: int) -> float:

    for a in range(n + 1): 
        for b in range(n + 1): 
            c_squared: int = a**2 + b**2
            c: float = c_squared**0.5
            if a < b and b < c and a + b + c == n: 
                return a * b * c
    return 0