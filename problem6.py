def rotate_string(s, k):
    """ (str,int) -> str
    
    Retuns the lexicographically smallest string 
    
    >>>rotate_string("daily",1)
    ailyd
    >>>rotate_string("daily",3)
    lyadi
    """
    sub = s[:k]
    sub_array = []
    for i in sub:
        sub_array.append(i)
    sub_array = sorted(sub_array)
    sub = ''
    for i in sub_array:
        sub += i
    return s[k:]+sub
    
    
    
s = input("enter the string")
k = int(input("enter the index"))
print(rotate_string(s,k))
