texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"] 
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
print("Palindromes present in the given list are:",end=" ")
print(result)