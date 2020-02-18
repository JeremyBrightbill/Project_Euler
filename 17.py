"""Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use 
of "and" when writing out numbers is in compliance with British usage."""

from typing import List

ones: dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens: dict = {0: '', 1: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', \
    6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
teens: dict = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: \
    'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}

def list_digits(n: int) -> List[int]:
    if n < 1 or n > 1000:
        raise ValueError("Number must be between 1 and 1000 inclusive")
    n_full = str(n).rjust(4, '0')
    return [int(value) for value in list(n_full)]

def number_to_words(n: int, ones: dict = ones, tens: dict = tens, teens: dict = teens) -> str:
    if n == 1000: 
        return 'onethousand'
    else: 
        num = list_digits(n)
        
        # Logic for hundreds
        if num[-3] == 0: 
            hundreds = ''
        elif num[-2] == 0 and num[-1] == 0: 
            hundreds = ones[num[-3]] + 'hundred'
        else:
            hundreds = ones[num[-3]] + 'hundredand'
        
        # Logic for tens and teens
        if num[-2] == 1: 
            tens = teens[num[-1]]
            ones = ''
        else: 
            tens = tens[num[-2]]
            ones = ones[num[-1]]
        
        return hundreds + tens + ones
    

if __name__ == "__main__":
    words = []
    for i in range(1, 1001):
        words.append(number_to_words(i))
    all_one = ''.join(words)
    print(len(all_one))