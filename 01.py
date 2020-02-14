"""If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


def find_sum_of_multiples(limit: int) -> int:
    loop_sum: int = 0
    for i in range(limit): 
        if i % 3 == 0 or i % 5 == 0: 
            loop_sum += i
    return loop_sum

def test_find_sum_of_multiples(): 
    assert find_sum_of_multiples(10) == 23

if __name__ == "__main__": 
    
    try: 
        test_find_sum_of_multiples()
    except(AssertionError): 
        print("Test failed")
    
    print(find_sum_of_multiples(1000))