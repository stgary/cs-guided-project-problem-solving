from typing import List

def csSumOfPositive(input_arr: List[int]) -> int:
  # Given an array of integers, return the sum of all the positive 
  # integers in the array
  # if the input_arr doesn't contain any positive integers
  # the default sum should be 0
  
  # make sum a variable with default value 0
  sum = 0
  
  # iterate through the list
  for v in input_arr:
  
  # use a python method or an if statement to determine if the number is
    if v < 0:
      continue
    else: 
      sum += v
  # positive or negative 
  # if it is positive add it to the sum (Like the JavaScript reduce())
  
  
  return sum

print(csSumOfPositive([1, 2, 3, -4, 5]))
print(csSumOfPositive([-3, -2, -1, 0, 1]))