def lsearch(arr, x): 
    for i in range(len(arr)): 
        if arr[i] == x: 
            return i 
    return -1
a=[34,6,7,12,8,10]
k=int(input("Enter the key element to be searched from the given list: "))
s=lsearch(a,k)
if(s!=-1):
    print(f"The given element {k} was found at {s+1} position.")
else:
    print(f"The given element {k} is not present in the given list.")