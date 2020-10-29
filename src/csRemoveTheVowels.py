def csRemoveTheVowels(input_str: str) -> str:
  # Given a string, return a new string with all the vowels removed
  # we need to inspect every character in the input string 
  # to see if it's a vowel 
  # string.translate method works for this occasion 
  return input_str.translate({ord(i): None for i in 'AEIOUaeiou'})

print(csRemoveTheVowels("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"))