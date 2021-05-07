def search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1
    
print(f"Element found at {search([1,2,3,4,5,6,7,8,9,10],4)} index")