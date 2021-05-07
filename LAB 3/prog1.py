def perfect(a):
    s = 0
    for i in range(1, a):
        if(a % i == 0):
             s = s + i
    if (s == a):
        return 1
    else:
        return 0
a=int(input("enter a number: "))
if(perfect(a)==1):
    print(f'{a} is a perfect number.')
else:
    print(f'{a} is not a perfect number.')