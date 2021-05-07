def binary_search(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2 
        if arr[mid] < x: 
            low = mid + 1 
        elif arr[mid] > x: 
            high = mid - 1 
        else: 
            return mid 
    return -1
arr = [ 2, 3, 4, 10, 40 ] 
x = int(input("Enter the key element to be searched from the given list: "))
result = binary_search(arr, x) 
if result != -1: 
    print(f"The given element {x} was found at {result+1} position.") 
else: 
    print("Element is not present in array") 