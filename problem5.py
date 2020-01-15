#Find palindrome in an array of strings

strings = ['da','d','mal','ayalam','dad']

def check (pal_check):
    rev_pal_check = pal_check[::-1]
    if (rev_pal_check == pal_check):
        return True
    else:
        return False

i=0
out = []
while i < (len(strings)-1):
    j = i+1
    while j <  len(strings):
        pal_check = strings[i] + strings[j]
        flag = check (pal_check)
        if (flag):
            out += [[i,j]]
        j+=1
    i+=1

print (out)
