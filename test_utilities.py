from utilities import find_prime_factors, find_primes, highest_power, is_prime, find_n_primes

def test_find_prime_factors(): 
    assert find_prime_factors(100) == [2, 2, 5, 5]
    assert find_prime_factors(76) == [2, 2, 19]
    assert find_prime_factors(50) == [2, 5, 5]
    assert find_prime_factors(48) == [2, 2, 2, 2, 3]
    assert find_prime_factors(36) == [2, 2, 3, 3]
    assert find_prime_factors(20) == [2, 2, 5]
    assert find_prime_factors(10) == [2, 5]

def test_find_primes(): 
    assert find_primes(10) == [2, 3, 5, 7]

def test_highest_power(): 
    assert highest_power(2, 10) == 8
    assert highest_power(3, 10) == 9
    assert highest_power(2, 5) == 4

def test_is_prime():
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False

def test_find_n_primes(): 
    assert find_n_primes(5) == [2, 3, 5, 7, 11]