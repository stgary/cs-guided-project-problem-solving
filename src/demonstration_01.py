"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""

from typing import List

def last(a: List[int], n: int) -> List[int]:
	# Your code here
	# if n is longer then the length of the list, return invalid
	if n > len(a):
        return "invalid"
    # we need to return the last n element as a list of integers
    
    # how would we do this is we needed to return the first n elements 
    # we'd want to grab everything starting from index 0 up to n
    # we'd want to grab a sublice where that subslice starts at 
    # the begining of our input list and has length n
    
    # python's slicing syntax 
    # a[0:n] - get first n elements
    # a[len(a) - n:] - get last n elements
    # start slicing from len(a) - n and then take everything 
    
    # JS/TS
    # a.slice(0, n)
    # a.slice(a.length - n)

print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))