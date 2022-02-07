s,t = [],[]
for i in range(int(input())):
    a = input().split()
    if a[0] == '1':
        s.append(a[1])
    else:
        t.append(s[0])
        s.pop(0)
print(*t)