def interleave (str1,str2):
    zipped_lists = list(zip(str1,str2))
    zipped_string =""
    for a in zipped_lists:
        zipped_string += "".join(a)
    return zipped_string

#with list comprehension
#def interleave(str1,str2):
#    return ''.join(''.join(x) for x in (zip(str1,str2)))

print(interleave("hi","ha"))