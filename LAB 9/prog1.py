def very_good(str1):
    string_very = str1.find('very')
    string_good = str1.find('good')
    
    if string_good>string_very and string_very>0 and string_good>0:
        str1 = str1.replace(str1[string_very:(string_good+4)],'excellent')
        return str1
    else:
        return str1
    
print(very_good("The essay is very good"))
