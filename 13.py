"""WORK IN PROGRESS

Work out the first ten digits of the sum of the following one-hundred 
50-digit numbers."""

import requests
from bs4 import BeautifulSoup
from typing import List

# Pull data straight from Project Euler page

URL = 'https://projecteuler.net/problem=13'

def get_data(URL: str) -> List[int]:
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, features='html.parser')
    nums = soup.select('[style*="font-size:10pt;text-align:center;"]')[0].text
    nums = nums.split('\n')
    nums = [int(value) for value in nums[1:]]
    return nums

if __name__ == "__main__":
    
    data = get_data(URL)
    print(sum(data))