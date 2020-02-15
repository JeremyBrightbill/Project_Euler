"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

from typing import List
from utilities import find_prime_factors

TARGET: int = 600851475143


if __name__ == "__main__":
    
    result: List[int] = find_prime_factors(TARGET)
    print(result[-1])