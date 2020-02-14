"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

from typing import List

TARGET: int = 600851475143

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

def test_find_prime_factors(): 
    assert find_prime_factors(100) == [2, 2, 5, 5]
    assert find_prime_factors(76) == [2, 2, 19]
    assert find_prime_factors(50) == [2, 5, 5]
    assert find_prime_factors(48) == [2, 2, 2, 2, 3]
    assert find_prime_factors(36) == [2, 2, 3, 3]
    assert find_prime_factors(20) == [2, 2, 5]
    assert find_prime_factors(10) == [2, 5]

if __name__ == "__main__":
    
    try: 
        test_find_prime_factors()
    except(AssertionError): 
        print("Test failed")
    else: 
        result: List[int] = find_prime_factors(TARGET)
        print(result[-1])