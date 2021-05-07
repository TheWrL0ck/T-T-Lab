n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Given list of integers:",end=" ")
print(n)
print("Square of every element in the given list:",end=" ")
square = list(map(lambda x: x ** 2, n))
print(square)
print("Cube of every element in the given list:",end=" ")
cube = list(map(lambda x: x ** 3, n))
print(cube)