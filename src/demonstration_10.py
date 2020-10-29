"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str: str) -> str:
    # Your code here
    # given a string of numbers, figure out the min and max
    # we have functions `max` and `min` which will find the max and min for us
    # works on non-negative numeric strings
    # it's feasible that we get a string of all negative numbers
    # because of negative numbers, we cant get away with not turning the string into numbers
    # how do we take the input string and turn it into a list of numbers?
    # we can split the input string on spaces
    str_digits = input_str.split(" ")
    int_digits = []
    
    for str_digit in str_digit:
        int_digit = int(str_digit)
        int_digits.append(int_digit)
        
    # calculate the min and max
    mx = max(int_digits)
    mn = min(int_digits)
    
    # use fstring to perform interpolation
    
    return f"{mx} {mn}"
    
    
print(max_and_min("1 2 3 4 5"))
print(max_and_min("1 2 -3 4 5"))
print(max_and_min("1 9 3 4 -5"))