"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
"""

from typing import List

def add_indexes(numbers: List[int]) -> List[int]:
    # Your code here
    # given a list of numbers output a new list
    # list where each of the list elements is the sum of the list
    # element with its corresponding index in
    output = [] 
    
    # iterate through list of numbers
    for i in range(len(numbers)):
        # get the ith number for this iteration
        n = numbers[i]
        # add the current number with its index
        sum = n + i
        # push that sum to a new list
        output.append(sum)

print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 4, 3, 2, 1]))