def fibSeries(nt):
    n1, n2 = 0, 1
    count = 0
    if nt <= 0:
        print("Please enter a positive integer")
    elif nt == 1:
        print("Fibonacci sequence upto",nt,":",end=" ")
        print(n1,end=" ")
    else:
        print("Fibonacci sequence:")
        while count < nt:
            print(n1,end=" ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1