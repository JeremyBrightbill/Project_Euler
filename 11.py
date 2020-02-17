"""In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

...

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid?

SOLUTION: Wanted to pull this with requests and BeautifulSoup, but the HTML is too irregular."""

import requests
from bs4 import BeautifulSoup

URL: str = 'https://projecteuler.net/problem=11'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
grid = soup.select('[style*="text-align:center;font-size:10pt;"]')

if __name__ == "__main__": 
    print(grid)