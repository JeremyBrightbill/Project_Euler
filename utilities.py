"""Utility functions for use in multiple programs"""

from typing import List
from math import sqrt, floor


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


# For Exercise 7 - IN PROGRESS

def is_prime(n: int) -> bool: 
    """Algorithm from Java at
https://algorithms.tutorialhorizon.com/print-first-n-prime-numbers-java-code/"""
    for i in range(2, floor(sqrt(n))):
        if n % i == 0: 
            return False
    return True

def find_n_primes(n: int) -> List:
    """Find the first n prime numbers"""
    number: int = 2
    primes: List[int] = []

    while len(primes) < n: 
        if is_prime(number): 
            primes.append(number)
        number += 1

    return primes
