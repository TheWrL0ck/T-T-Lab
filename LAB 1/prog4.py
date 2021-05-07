a=str(input("Enter a string:-"))
x=0
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o'or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        x=x+1
print(f'No of vowels in the given string={x}')