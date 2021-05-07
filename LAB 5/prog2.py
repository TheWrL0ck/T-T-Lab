n = [1, 99, 46, 28, 31, 63, 50]
print("Odd numbers from the said list:",end=" ")
on = list(filter(lambda x: x%2 != 0, n))
print(on)