s = input()
t = ''
mylist = []
for i in range(len(s)):
    if s[i]!=' ':
        t+=s[i]
    if i==len(s)-1:
        if len(t)>=3:
            mylist.append(t)
    if s[i]==' ':
        if len(t)>=3:
            mylist.append(t)
        t=''

print(*mylist)