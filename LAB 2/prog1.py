def fact(n):
    f=1
    while(n!=1):
        f=f*n
        n=n-1
    return f
l=int(input("enter a number "))
k=fact(l)
print(f"factorial of {l} = {k}")