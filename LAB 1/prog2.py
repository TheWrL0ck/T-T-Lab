def maxi(li):
    x=0
    for i in li:
        if x<i:
            x=i
    return x
l1=[1,2,3,4,5]
a=maxi(l1)
print(f'Maximum element in the list={a}')