s = input()
t = input()
mylist = []
for i in range(len(s)):
    if s[i] == t:
        mylist.append(i)

if len(mylist)>1:
    print(mylist[0],mylist[len(mylist)-1])
else:
    print(*mylist)