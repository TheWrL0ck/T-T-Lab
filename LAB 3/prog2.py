def isPangram(s):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in s:
         return False
   return True
s = input("enter a string: ")
if(isPangram(s)):
   print(f'The given string {s} is a pangram')
else:
   print(f'The given string {s} is not a pangram')