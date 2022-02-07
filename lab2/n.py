n = 1
l,d,s = [],[],[]
while(n == 1):
    a = int(input())
    if a == 0:
        break
    l.append(a)
for i in range(len(l)):
    if i < int(len(l)/2):
        d.append(l[i])
    else:
        s.append(l[i])
s = s[::-1]
l.clear()
if len(s)>len(d):
    l.append(s[-1])
    s.pop()
for i in range(len(s)):
    print(str(s[i]+d[i])+' ',end='')
print(*l)