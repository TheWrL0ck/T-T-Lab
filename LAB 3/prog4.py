def countUL(string): 
    count1=0
    count2=0
    for i in string:
        if(i.islower()):
             count1=count1+1
        elif(i.isupper()):
             count2=count2+1 
    print(f'No. of lowercase characters= {count1}')
    print(f'No. of uppercase characters= {count2}')
s=input("enter a string: ")
countUL(s)