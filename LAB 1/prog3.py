def isPal(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input("Enter a string:-")
ans = isPal(s)
if ans:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")