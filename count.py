n=input('enter the word')
s=n.split( )
print(s)
dict=dict()
set=list(set(s))
print(set)
for i in set:
    if i in s:
        dict[i]=s.count(i)
print(dict)    
