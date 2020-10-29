def csLongestPossible(str_1: str, str_2: str) -> str:
  # Given two strings that include only lower case alpha
  # characters, str_1 and str_2, write a function that
  # returns a new soreted string that contains any character (only once)
  # that appeared in str_1 or str_2
  
  # define an empty string to keep chars 
  output = ""
  
  # iterate over the strings
  for char in str_1:    
    # write an if statement that evaluates if the string is in the output string  
    if char in output:
      continue
    else:
      output += char
  # repeat because I cant figure out how to reduce it down to one for loop
  for char in str_2:
    
    if char in output:
      continue
    else:
      output += char
      
    
  
  return ''.join(sorted(output))

print(csLongestPossible(csLongestPossible("aabbbcccdef", "xxyyzzz")))