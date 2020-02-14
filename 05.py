"""2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?

IN PROGRESS. This solution works but isn't efficient."""


N: int = 20

def find_if_divisible(n: int) -> int:
    """Find the smallest number divisible by all numbers from 1 to n. 
    Since every number is divisible by 1, start testing at 2.
    Speed up by only considering multiples of 19 * 20 = 380"""
    counter: int = 380
    while True: 
        if all([counter % i == 0 for i in range(2, n+1)]):
            break
        else: 
            counter += 380
            if counter % 1000 == 0:
                print(counter)
    return counter

if __name__ == "__main__":
    
    print(find_if_divisible(N))