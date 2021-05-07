def tuple_to_int(nums):
    result = int(''.join(map(str,nums)))
    return result
nums = (1,2,3,4,5)
print("Original tuple: ") 
print(nums)
print("Convert the said tuple of positive integers into an integer:")
print(tuple_to_int(nums))