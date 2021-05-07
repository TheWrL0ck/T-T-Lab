def very_good(str1):
    svery = str1.find('very')
    sgood = str1.find('good')
    
    if sgood>svery and svery>0 and sgood>0:
        str1 = str1.replace(str1[svery:(sgood+4)],'excellent')
        return str1
    else:
        return str1
print(very_good("The essay is very good"))