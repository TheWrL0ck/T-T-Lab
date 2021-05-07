def remKthChar(s,k):
    a=s[:k-1]
    b=s[k:]
    print(f"After removing the {k}th character from {s} we get = {a+b}")
s=input("enter a string ")
k=int(input("enter the character to be removed "))
remKthChar(s,k)