"""Given a word w and a string s, find and return a list of all 
the indices in s which are  the starting locations of anagrams of w"""

w = 'ab'
s = 'abxaba'
o = []

s_len = len(s)
w_len = len(w)
s_rev = s[s_len::-1]

i = 0
while i < s_len:
    bundle1 = s[i:i+w_len]
    if(w == bundle1):
        o.append(i)

    bundle2 = s_rev[i:i+w_len]
    if(w == bundle2):
       o.append (s_len - (i+w_len))
    
    i += 1
 
o.sort()    
print(o)
