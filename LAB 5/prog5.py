num = [-1,2,5,-7,13,-8]
positive = list(filter(lambda x: x>0,num))
negative = list(filter(lambda x: x<0,num))
print(positive+negative)