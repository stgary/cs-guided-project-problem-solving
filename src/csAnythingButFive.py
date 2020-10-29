def csAnythingButFive(start: int, end: int) -> int:
  # Given a start integer and an ending integer
  # (both inclusive), write a function that returns a count
  # (not the sum) of all the integers in the range
  # (except integers that contain 5)
  
  # make a count variable set it to 0 
  count = 0
  
  # iterate through the range starting with start input and 
  # ending with end input
  for i in range(start, end + 1):
    
    # if statement that checks for the digit 5 in it
    if str(5) in str(i):
      
    # if it does contain the digit 5 then continue
      continue
    
    # if it doesnt then increment count ++1
    else:
      
      count += 1 
      
    print(i)   
  
  # return count
  return count

print(csAnythingButFive(1, 90))