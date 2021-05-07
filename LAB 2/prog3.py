def minChar(s):
    all_freq = {} 
    for i in s: 
        if i in all_freq: 
           all_freq[i] += 1
        else: 
           all_freq[i] = 1
    res = min(all_freq, key = all_freq.get)
    return res
str="aabbccdde"
k=minChar(str)
print(f"the minimum character present in the string {str} = {k}")