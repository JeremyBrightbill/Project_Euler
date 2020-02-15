from utilities import find_primes, highest_power

def test_find_primes(): 
    assert find_primes(10) == [2, 3, 5, 7]

def test_highest_power(): 
    assert highest_power(2, 10) == 8
    assert highest_power(3, 10) == 9
    assert highest_power(2, 5) == 4