def csShortestWord(input_str: str) -> int:
  # Given a string of words, return the length of the shortest word(s)
  # The input string will never be empty and you do not need to validate for different data types
  # is there a python method to find the shortest? No
  # use the len and split functions in unisone
  l = map(len, input_str.split())
  
  return min(l)

print(csShortestWord("not great programmer; just good programmer with great habits."))